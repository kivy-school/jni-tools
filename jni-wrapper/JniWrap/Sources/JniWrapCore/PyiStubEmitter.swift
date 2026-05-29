import Foundation

/// Emits a PEP-484 `.pyi` stub file with Pythonic types for each pyjnius
/// wrapper class. Goals:
///
/// 1. Every annotation in the stub must be **resolvable** by the IDE.
///    A quoted forward ref pointing at a name that isn't defined anywhere
///    just collapses to `Any` *plus* raises an "unresolved reference"
///    warning — worst of both worlds.
/// 2. For wrapped types in another `.py` file we emit a real
///    `from x.y.z import Foo` and use the bare name.
/// 3. For same-file nested types (e.g. `Builder`, `Companion`, `UseThread`)
///    we use quoted forward refs — pyright/mypy resolve those because the
///    symbol exists in the same module.
/// 4. For everything else (unwrapped externals like `android.app.Activity`,
///    `java.lang.Runnable`, `android.os.Bundle`) we **synthesize a
///    methodless stub class at the top of the `.pyi`** and bind the
///    annotation to that. The IDE sees a real type with the right simple
///    name instead of `Any`. A comment records the Java FQCN so the reader
///    can find it.
/// 5. `Any` is the absolute last resort (e.g. `java.lang.Object`, or an
///    unrepresentable type).
public struct PyiStubEmitter {

    /// Information the emitter needs to convert Java FQCNs into Pythonic
    /// annotations + decide which imports to add at the top of the stub.
    public struct Resolution {
        /// FQCNs of top-level classes that have their own generated `.py`
        /// file. These are the only things we can `from … import` from.
        public var topLevelFqcns: Swift.Set<String>
        /// FQCNs of every wrapped type (top-level + nested).
        public var allFqcns: Swift.Set<String>
        /// Given a top-level FQCN, return the dotted Python module path
        /// (e.g. `"android.gms.ads.MobileAds"`) for the file we emit.
        public var modulePath: (String) -> String?
        /// Maps a Java package prefix (must end with `.`, e.g. `"android."`)
        /// to an existing Python module prefix (e.g. `"android"`). When an
        /// otherwise-unresolved class FQCN starts with `javaPrefix`, the
        /// emitter imports it from `<pyPrefix>.<subpkg>.<Simple>` instead
        /// of synthesizing a forward-declared stub. Mirrors the per-class
        /// layout produced by `jni-wrap --keep-package-prefix`.
        public var externalModules: [(javaPrefix: String, pyPrefix: String)]

        public init(topLevelFqcns: Swift.Set<String> = [],
                    allFqcns: Swift.Set<String> = [],
                    modulePath: @escaping (String) -> String? = { _ in nil },
                    externalModules: [(javaPrefix: String, pyPrefix: String)] = []) {
            self.topLevelFqcns = topLevelFqcns
            self.allFqcns = allFqcns
            self.modulePath = modulePath
            self.externalModules = externalModules
        }
    }

    public init() {}

    /// Render a `.pyi` stub for a single top-level class (with nested types
    /// embedded as nested `class` blocks).
    public func render(_ cls: ClassNode,
                       resolution: Resolution = .init()) -> String {
        let selfNames = Self.collectSimpleNames(in: cls)
        var imports: [(module: String, name: String)] = []
        var importKeys = Swift.Set<String>()
        // External class refs that aren't wrapped, not built-in, not same-file.
        // simpleName → FQCN of the FIRST occurrence (collisions across
        // different packages keep the first; comment shows which one).
        var externals: [String: String] = [:]
        var externalOrder: [String] = []

        func addImport(_ module: String, _ name: String) {
            let key = "\(module):\(name)"
            if importKeys.insert(key).inserted {
                imports.append((module, name))
            }
        }

        func mapRef(_ fqcn: String) -> String {
            if fqcn.hasSuffix("[]") {
                let inner = mapRef(String(fqcn.dropLast(2)))
                // If the inner type is unresolvable we'd produce `list[Any]`
                // which is no more informative than a bare `list` — and a
                // bare `list` is what Java arrays of unknowns actually map
                // to at runtime via pyjnius anyway.
                return inner == "Any" ? "list" : "list[\(inner)]"
            }
            if let mapped = Self.builtinMap[fqcn] { return mapped }
            // Reference type. Decide bucket.
            let simple = fqcn.split(separator: ".").last.map(String.init) ?? fqcn
            // Same-file nested ref: quoted forward ref resolves against the
            // enclosing module.
            if resolution.allFqcns.contains(fqcn) && selfNames.contains(simple) {
                return "\"\(simple)\""
            }
            // Cross-file wrapped: real import + bare name.
            if resolution.topLevelFqcns.contains(fqcn),
               let module = resolution.modulePath(fqcn) {
                addImport(module, simple)
                return simple
            }
            // External package mapping (e.g. android.* lives in a separate
            // pre-wrapped `android-pyjnius` package). Import from there
            // instead of stubbing.
            for (javaPrefix, pyPrefix) in resolution.externalModules {
                guard fqcn.hasPrefix(javaPrefix) else { continue }
                let tail = String(fqcn.dropFirst(javaPrefix.count))
                let parts = tail.split(separator: ".").map(String.init)
                guard let last = parts.last,
                      Self.isValidIdentifier(last),
                      !selfNames.contains(last) else { continue }
                let sub = parts.dropLast().joined(separator: ".")
                let module: String
                if sub.isEmpty {
                    module = "\(pyPrefix).\(last)"
                } else {
                    module = "\(pyPrefix).\(sub).\(last)"
                }
                addImport(module, last)
                return last
            }
            // Unwrapped external: synthesize a forward-declared stub class
            // at the top of this file so the name actually resolves.
            if Self.isValidIdentifier(simple) && !selfNames.contains(simple) {
                if externals[simple] == nil {
                    externals[simple] = fqcn
                    externalOrder.append(simple)
                }
                return simple
            }
            // Last resort.
            return "Any"
        }

        var body: [String] = []
        appendClass(cls, indent: "", into: &body, mapRef: mapRef)

        // Header: typing, imports, external forward-decl stubs, body.
        var lines: [String] = ["from typing import Any, ClassVar, overload"]
        let sortedImports = imports.sorted {
            $0.module == $1.module ? $0.name < $1.name : $0.module < $1.module
        }
        for imp in sortedImports {
            lines.append("from \(imp.module) import \(imp.name)")
        }
        if !externalOrder.isEmpty {
            lines.append("")
            lines.append("# Forward declarations for Java types we do not wrap.")
            lines.append("# Bound as empty classes so annotations resolve in the IDE.")
            for name in externalOrder {
                let fqcn = externals[name] ?? name
                lines.append("class \(name):")
                lines.append("    \"\"\"Forward declaration for ``\(fqcn)``.")
                lines.append("")
                lines.append("    This Java type is referenced by the wrapper but is not itself")
                lines.append("    wrapped by jni-wrap. At runtime pyjnius will hand you a")
                lines.append("    live ``autoclass('\(fqcn)')`` proxy; this empty class exists")
                lines.append("    purely so static type checkers and IDEs can resolve the name.")
                if let url = Self.javadocURL(for: fqcn) {
                    lines.append("")
                    lines.append("    See: \(url)")
                }
                lines.append("    \"\"\"")
                lines.append("    ...")
            }
        }
        lines.append("")
        lines.append(contentsOf: body)
        return lines.joined(separator: "\n") + "\n"
    }

    // MARK: - Class body

    private func appendClass(_ cls: ClassNode,
                             indent: String,
                             into lines: inout [String],
                             mapRef: (String) -> String) {
        lines.append("\(indent)class \(cls.simpleName):")
        let body = indent + "    "
        var produced = false

        if cls.kind == .enumType, let constants = cls.enumConstants {
            for ec in constants {
                lines.append("\(body)\(ec.name): ClassVar[\"\(cls.simpleName)\"]")
                produced = true
            }
        }

        for f in cls.fields where f.isStatic {
            lines.append("\(body)\(safeName(f.name)): ClassVar[\(mapRef(f.typeFqcn))]")
            produced = true
        }
        for f in cls.fields where !f.isStatic {
            lines.append("\(body)\(safeName(f.name)): \(mapRef(f.typeFqcn))")
            produced = true
        }

        if cls.kind != .interfaceType && !cls.constructors.isEmpty {
            if cls.constructors.count == 1 {
                let c = cls.constructors[0]
                let params = formatParams(c.parameters, varargs: c.isVarargs,
                                          includeSelf: true, mapRef: mapRef)
                lines.append("\(body)def __init__\(params) -> None: ...")
            } else {
                for c in cls.constructors {
                    lines.append("\(body)@overload")
                    let params = formatParams(c.parameters, varargs: c.isVarargs,
                                              includeSelf: true, mapRef: mapRef)
                    lines.append("\(body)def __init__\(params) -> None: ...")
                }
            }
            produced = true
        }

        var order: [String] = []
        var bucket: [String: [MethodNode]] = [:]
        for m in cls.methods {
            if bucket[m.name] == nil { order.append(m.name) }
            bucket[m.name, default: []].append(m)
        }
        for name in order {
            let methods = bucket[name]!
            let safe = safeName(name)
            if methods.count == 1 {
                emitMethod(methods[0], pyName: safe, body: body,
                           overload: false, mapRef: mapRef, into: &lines)
            } else {
                for m in methods {
                    emitMethod(m, pyName: safe, body: body,
                               overload: true, mapRef: mapRef, into: &lines)
                }
            }
            produced = true
        }

        for n in cls.nested {
            lines.append("")
            appendClass(n, indent: body, into: &lines, mapRef: mapRef)
            produced = true
        }

        if !produced {
            lines.append("\(body)...")
        }
    }

    private func emitMethod(_ m: MethodNode, pyName: String, body: String,
                            overload: Bool,
                            mapRef: (String) -> String,
                            into lines: inout [String]) {
        if overload { lines.append("\(body)@overload") }
        if m.isStatic { lines.append("\(body)@staticmethod") }
        let params = formatParams(m.parameters, varargs: m.isVarargs,
                                  includeSelf: !m.isStatic, mapRef: mapRef)
        let ret = mapRef(m.returnTypeFqcn)
        lines.append("\(body)def \(pyName)\(params) -> \(ret): ...")
    }

    private func formatParams(_ params: [ParamNode],
                              varargs: Bool,
                              includeSelf: Bool,
                              mapRef: (String) -> String) -> String {
        var parts: [String] = []
        if includeSelf { parts.append("self") }
        let last = params.count - 1
        for (i, p) in params.enumerated() {
            let name = safeParamName(p.name, idx: i)
            if varargs && i == last && p.typeFqcn.hasSuffix("[]") {
                let inner = mapRef(String(p.typeFqcn.dropLast(2)))
                parts.append("*\(name): \(inner)")
            } else {
                parts.append("\(name): \(mapRef(p.typeFqcn))")
            }
        }
        return "(" + parts.joined(separator: ", ") + ")"
    }

    // MARK: - Helpers

    /// Simple names of `cls` and every nested type, recursively. These are
    /// the identifiers a quoted forward ref inside this stub can legally
    /// point at.
    private static func collectSimpleNames(in cls: ClassNode) -> Swift.Set<String> {
        var names: Swift.Set<String> = [cls.simpleName]
        for n in cls.nested {
            names.formUnion(collectSimpleNames(in: n))
        }
        return names
    }

    private static func isValidIdentifier(_ s: String) -> Bool {
        guard let first = s.first else { return false }
        guard first.isLetter || first == "_" else { return false }
        return s.allSatisfy { $0.isLetter || $0.isNumber || $0 == "_" }
    }

    /// Best-effort JavaDoc URL for an external FQCN. Returns nil when we
    /// don't have a reliable doc host for that namespace.
    internal static func javadocURL(for fqcn: String) -> String? {
        // Drop any trailing `[]` and nested-class `$` markers (we never use
        // `$` here but be defensive).
        var clean = fqcn
        while clean.hasSuffix("[]") { clean.removeLast(2) }
        clean = clean.replacingOccurrences(of: "$", with: ".")
        let slashed = clean.replacingOccurrences(of: ".", with: "/")
        if clean.hasPrefix("android.") || clean.hasPrefix("androidx.")
            || clean.hasPrefix("dalvik.") {
            return "https://developer.android.com/reference/\(slashed)"
        }
        if clean.hasPrefix("java.") || clean.hasPrefix("javax.")
            || clean.hasPrefix("org.w3c.") || clean.hasPrefix("org.xml.") {
            // Stable classic JavaDoc — every java.* / javax.* class has a
            // page at this host, no module path needed.
            return "https://docs.oracle.com/javase/8/docs/api/\(slashed).html"
        }
        if clean.hasPrefix("kotlin.") || clean.hasPrefix("kotlinx.") {
            return "https://kotlinlang.org/api/latest/jvm/stdlib/\(slashed)/"
        }
        if clean.hasPrefix("com.google.android.gms.")
            || clean.hasPrefix("com.google.firebase.") {
            return "https://developers.google.com/android/reference/\(slashed)"
        }
        return nil
    }

    private func safeParamName(_ name: String, idx: Int) -> String {
        let n = name.isEmpty ? "arg\(idx)" : name
        return safeName(n)
    }

    private func safeName(_ s: String) -> String {
        Self.pyKeywords.contains(s) ? s + "_" : s
    }

    private static let pyKeywords: Swift.Set<String> = [
        "False","None","True","and","as","assert","async","await","break","class",
        "continue","def","del","elif","else","except","finally","for","from","global",
        "if","import","in","is","lambda","nonlocal","not","or","pass","raise","return",
        "try","while","with","yield","match","case"
    ]

    /// Built-in mapping table — fixed conversions only. Misses fall through
    /// to `Resolution`-aware logic in `mapRef`.
    private static let builtinMap: [String: String] = [
        "void": "None",
        "boolean": "bool",
        "byte": "int", "short": "int", "int": "int", "long": "int",
        "float": "float", "double": "float",
        "char": "str",
        "java.lang.String": "str",
        "java.lang.CharSequence": "str",
        "java.lang.Object": "Any",
        "java.lang.Boolean": "bool",
        "java.lang.Integer": "int", "java.lang.Long": "int",
        "java.lang.Short": "int", "java.lang.Byte": "int",
        "java.lang.Float": "float", "java.lang.Double": "float",
        "java.lang.Number": "float",
        "java.lang.Character": "str",
        "java.util.List": "list", "java.util.Collection": "list",
        "java.util.ArrayList": "list", "java.util.LinkedList": "list",
        "java.util.Map": "dict", "java.util.HashMap": "dict",
        "java.util.LinkedHashMap": "dict", "java.util.TreeMap": "dict",
        "java.util.Set": "set", "java.util.HashSet": "set",
        "java.util.LinkedHashSet": "set", "java.util.TreeSet": "set",
        "java.lang.Class": "type",
    ]
}
