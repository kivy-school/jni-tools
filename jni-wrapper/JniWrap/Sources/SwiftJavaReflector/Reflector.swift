import Foundation
import JniWrapCore
import SwiftJava
import JavaLangReflect
import JavaUtilJar
import JavaNet

// MARK: - Java modifier bit masks
private enum JavaModifierBits {
    static let `public`:    Int32 = 0x0001
    static let `private`:   Int32 = 0x0002
    static let `protected`: Int32 = 0x0004
    static let `static`:    Int32 = 0x0008
    static let `final`:     Int32 = 0x0010
    static let `abstract`:  Int32 = 0x0400
    static let `interface`: Int32 = 0x0200
    static let `enum`:      Int32 = 0x4000
}

// MARK: - Reflector

/// Reflects on Java classes in a JAR/AAR using an in-process JVM (via swift-java 0.3.0)
/// and produces a `JniWrapCore.AstDocument`.
public struct Reflector: Sendable {

    /// Configuration for the reflector.
    public struct Config: Sendable {
        /// Path to the JAR or AAR file to reflect on.
        public var inputPath: URL
        /// Additional classpath entries (e.g., dependent JARs).
        public var additionalClasspath: [URL]

        public init(inputPath: URL, additionalClasspath: [URL] = []) {
            self.inputPath = inputPath
            self.additionalClasspath = additionalClasspath
        }
    }

    public init() {}

    /// Reflects on all public classes in the given JAR/AAR and returns an `AstDocument`.
    public func reflect(config: Config) throws -> AstDocument {
        // 1. Resolve the JAR to use (extract classes.jar from AAR if needed).
        let jarURL = try resolveJar(from: config.inputPath)
        defer { cleanupTempJar(jarURL, originalInput: config.inputPath) }

        // 2. Build the full classpath: the JAR + any additional entries.
        var classpath = [jarURL.path]
        classpath += config.additionalClasspath.map(\.path)

        // 3. Boot (or reuse) the shared JVM.
        let jvm: JavaVirtualMachine
        do {
            jvm = try JavaVirtualMachine.shared(classpath: classpath)
        } catch {
            throw ReflectorError.jvmBootFailed(String(describing: error))
        }
        let env = try jvm.environment()

        // 4. Enumerate class names from the JAR.
        let classNames = try enumerateClassNames(jarPath: jarURL.path, environment: env)

        // 5. Load each class via reflection and convert to ClassNode.
        var classes: [ClassNode] = []
        let javaClassMeta = try JavaClass<JavaClass<JavaObject>>(environment: env)

        for className in classNames {
            // Skip inner/anonymous/synthetic classes at the top level; they are
            // picked up as nested classes on their enclosing class.
            guard !className.contains("$") else { continue }

            do {
                guard let cls = try javaClassMeta.forName(className) else { continue }
                if let node = try buildClassNode(cls, environment: env) {
                    classes.append(node)
                }
            } catch {
                // Log and continue — a missing dependency shouldn't abort the whole run.
                fputs("[warning] Failed to load class '\(className)': \(error)\n", stderr)
            }
        }

        return AstDocument(classes: classes)
    }
}

// MARK: - JAR resolution (handle AAR)

extension Reflector {

    /// Returns a URL to a usable JAR file.
    /// For `.aar` inputs, extracts `classes.jar` to a temp directory.
    private func resolveJar(from input: URL) throws -> URL {
        let ext = input.pathExtension.lowercased()
        guard ext == "aar" else {
            return input
        }
        // Extract classes.jar from the AAR (which is a ZIP).
        let tmpDir = FileManager.default.temporaryDirectory
            .appendingPathComponent("reflector-\(UUID().uuidString)", isDirectory: true)
        try FileManager.default.createDirectory(at: tmpDir, withIntermediateDirectories: true)

        let result = runProcess("/usr/bin/unzip", args: ["-o", input.path, "classes.jar", "-d", tmpDir.path])
        guard result == 0 else {
            throw ReflectorError.noClassesJarInAar(input.path)
        }
        let classesJar = tmpDir.appendingPathComponent("classes.jar")
        guard FileManager.default.fileExists(atPath: classesJar.path) else {
            throw ReflectorError.noClassesJarInAar(input.path)
        }
        return classesJar
    }

    /// Removes the temp directory if we created one for an AAR.
    private func cleanupTempJar(_ jar: URL, originalInput: URL) {
        guard originalInput.pathExtension.lowercased() == "aar" else { return }
        try? FileManager.default.removeItem(at: jar.deletingLastPathComponent())
    }

    private func runProcess(_ executable: String, args: [String]) -> Int32 {
        let proc = Process()
        proc.executableURL = URL(fileURLWithPath: executable)
        proc.arguments = args
        proc.standardOutput = FileHandle.nullDevice
        proc.standardError = FileHandle.nullDevice
        try? proc.run()
        proc.waitUntilExit()
        return proc.terminationStatus
    }
}

// MARK: - Class name enumeration

extension Reflector {

    /// Enumerates all `.class` entry names in a JAR and converts them to
    /// binary class names (e.g. `"com/example/Foo.class"` → `"com.example.Foo"`).
    private func enumerateClassNames(jarPath: String, environment env: JNIEnvironment) throws -> [String] {
        let jarFile = try JarFile(jarPath, environment: env)
        guard let entries = jarFile.entries() else { return [] }

        var names: [String] = []
        for entry in entries {
            let name = entry.getName()
            guard name.hasSuffix(".class"), !name.hasSuffix("module-info.class") else { continue }
            // Convert "com/example/Foo.class" → "com.example.Foo"
            let className = String(name.dropLast(6)).replacingOccurrences(of: "/", with: ".")
            names.append(className)
        }
        return names
    }
}

// MARK: - ClassNode construction

extension Reflector {

    private func buildClassNode(
        _ cls: JavaClass<JavaObject>,
        environment env: JNIEnvironment
    ) throws -> ClassNode? {
        let mods = cls.getModifiers()

        // Skip non-public classes.
        guard (mods & JavaModifierBits.public) != 0 else { return nil }

        let fqcn = cls.getName()
        let simpleName = cls.getSimpleName()
        let jniName = JNIDescriptor.jniName(from: fqcn)

        let kind: ClassKind
        if cls.isEnum() {
            kind = .enumType
        } else if cls.isInterface() {
            kind = .interfaceType
        } else {
            kind = .classType
        }

        let classModifiers = modifiers(from: mods)

        let superclass: String?
        if let sc = cls.getSuperclass() {
            let scName = sc.getName()
            superclass = scName == "java.lang.Object" ? nil : scName
        } else {
            superclass = nil
        }

        let interfaces: [String] = cls.getInterfaces().compactMap { $0?.getName() }

        // Public fields (getFields() returns public fields including inherited).
        let fields: [FieldNode] = cls.getFields().compactMap { field -> FieldNode? in
            guard let field else { return nil }
            let fmods = field.getModifiers()
            guard (fmods & JavaModifierBits.public) != 0 else { return nil }
            let typeName = field.getType()?.getName() ?? "java.lang.Object"
            let isStatic = (fmods & JavaModifierBits.static) != 0
            return FieldNode(
                name: field.getName(),
                jniDescriptor: JNIDescriptor.descriptor(forClassName: typeName),
                typeFqcn: typeName,
                isStatic: isStatic,
                modifiers: modifiers(from: fmods),
                javadoc: nil
            )
        }

        // Public constructors.
        let constructors: [ConstructorNode] = cls.getConstructors().compactMap { ctor -> ConstructorNode? in
            guard let ctor else { return nil }
            let cmods = ctor.getModifiers()
            let paramTypes = ctor.getParameterTypes()
            let params = paramNodes(from: paramTypes)
            let paramDescs = paramTypes.map { JNIDescriptor.descriptor(forClassName: $0?.getName() ?? "java.lang.Object") }
            let jniSig = "(\(paramDescs.joined()))V"
            let isVarargs = ctor.isVarArgs()
            return ConstructorNode(
                jniDescriptor: jniSig,
                isVarargs: isVarargs,
                modifiers: modifiers(from: cmods),
                parameters: params,
                javadoc: nil
            )
        }

        // Declared methods (getDeclaredMethods includes all visibility).
        let methods: [MethodNode] = cls.getDeclaredMethods().compactMap { method -> MethodNode? in
            guard let method else { return nil }
            let mmods = method.getModifiers()
            guard (mmods & JavaModifierBits.public) != 0 else { return nil }
            let returnTypeName = method.getReturnType()?.getName() ?? "void"
            let paramTypes = method.getParameterTypes()
            let params = paramNodes(from: paramTypes)
            let paramDescs = paramTypes.map { JNIDescriptor.descriptor(forClassName: $0?.getName() ?? "java.lang.Object") }
            let retDesc = JNIDescriptor.descriptor(forClassName: returnTypeName)
            let jniSig = "(\(paramDescs.joined()))\(retDesc)"
            let isStatic = (mmods & JavaModifierBits.static) != 0
            let isVarargs = method.isVarArgs()
            return MethodNode(
                name: method.getName(),
                jniDescriptor: jniSig,
                isStatic: isStatic,
                isVarargs: isVarargs,
                modifiers: modifiers(from: mmods),
                parameters: params,
                returnTypeFqcn: returnTypeName,
                javadoc: nil
            )
        }

        // Nested classes (public only).
        let nested: [ClassNode] = try cls.getDeclaredClasses().compactMap { inner -> ClassNode? in
            guard let inner else { return nil }
            return try buildClassNode(inner, environment: env)
        }

        // Enum constants: look for public static final fields whose type matches the class itself.
        var enumConstants: [EnumConstantNode]? = nil
        if cls.isEnum() {
            enumConstants = cls.getFields().compactMap { field -> EnumConstantNode? in
                guard let field else { return nil }
                let fmods = field.getModifiers()
                let isEnumConst = (fmods & JavaModifierBits.public) != 0 &&
                                  (fmods & JavaModifierBits.static) != 0 &&
                                  (fmods & JavaModifierBits.final) != 0 &&
                                  field.getType()?.getName() == fqcn
                guard isEnumConst else { return nil }
                return EnumConstantNode(name: field.getName(), javadoc: nil)
            }
        }

        return ClassNode(
            fqcn: fqcn,
            jniName: jniName,
            simpleName: simpleName,
            kind: kind,
            modifiers: classModifiers,
            superclass: superclass,
            interfaces: interfaces,
            javadoc: nil,
            fields: fields,
            constructors: constructors,
            methods: methods,
            nested: nested,
            enumConstants: enumConstants
        )
    }

    private func paramNodes(from types: [JavaClass<JavaObject>?]) -> [ParamNode] {
        types.enumerated().compactMap { (idx, cls) -> ParamNode? in
            guard let cls else { return nil }
            let typeName = cls.getName()
            return ParamNode(
                name: "p\(idx)",
                jniDescriptor: JNIDescriptor.descriptor(forClassName: typeName),
                typeFqcn: typeName
            )
        }
    }

    private func modifiers(from bits: Int32) -> [JavaModifier] {
        var result: [JavaModifier] = []
        if (bits & JavaModifierBits.public)    != 0 { result.append(.public) }
        if (bits & JavaModifierBits.protected) != 0 { result.append(.protected) }
        if (bits & JavaModifierBits.private)   != 0 { result.append(.private) }
        if (bits & JavaModifierBits.static)    != 0 { result.append(.static) }
        if (bits & JavaModifierBits.final)     != 0 { result.append(.final) }
        if (bits & JavaModifierBits.abstract)  != 0 { result.append(.abstract) }
        return result
    }
}

// MARK: - Errors

public enum ReflectorError: Error, CustomStringConvertible {
    case notImplemented(String)
    case noClassesJarInAar(String)
    case jvmBootFailed(String)
    case classLoadFailed(String, underlying: Error)

    public var description: String {
        switch self {
        case .notImplemented(let msg):
            return "Reflector not implemented: \(msg)"
        case .noClassesJarInAar(let path):
            return "No classes.jar found in AAR: \(path)"
        case .jvmBootFailed(let msg):
            return "Failed to boot embedded JVM: \(msg)"
        case .classLoadFailed(let className, let err):
            return "Failed to load class '\(className)': \(err)"
        }
    }
}

