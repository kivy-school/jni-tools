import Foundation
import PyjniusWrapCore
import SwiftJava
import JavaLangReflect
import JavaUtilJar
import JavaNet

/// Reflects on Java classes in a JAR (or .aar) file using an embedded JVM via swift-java,
/// producing `[ClassNode]` compatible with `PyjniusWrapCore.Schema`.
///
/// This replaces the external `java-ast-emitter.jar` subprocess by performing reflection
/// directly in-process using swift-java's embedded JVM.
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

    /// Reflects on all classes in the given JAR/AAR and returns an `AstDocument`.
    ///
    /// For `.aar` files, this extracts `classes.jar` to a temporary location first.
    public func reflect(config: Config) throws -> AstDocument {
        let jarURL = try resolveJarPath(config.inputPath)
        let classpath = buildClasspath(jarURL: jarURL, additional: config.additionalClasspath)

        // Boot the embedded JVM with the target JAR on the classpath.
        let jvm = try JavaVirtualMachine.shared(classpath: classpath)
        let environment = try jvm.environment()

        // Enumerate all class names in the JAR file.
        let classNames = try enumerateClassNames(jarPath: jarURL.path, environment: environment)

        // Load each class and reflect on it.
        var classNodes: [ClassNode] = []
        for className in classNames {
            // Skip anonymous/synthetic classes.
            if className.contains("$") && className.split(separator: "$").last?.first?.isNumber == true {
                continue
            }
            do {
                let node = try reflectClass(className: className, environment: environment)
                // Only emit top-level classes (not inner classes, which we get via nested).
                if !className.contains("$") {
                    classNodes.append(node)
                }
            } catch {
                // Skip classes that fail to load (e.g., missing dependencies).
                continue
            }
        }

        return AstDocument(classes: classNodes)
    }

    // MARK: - Private Implementation

    /// For .aar files, extract classes.jar; otherwise return as-is.
    private func resolveJarPath(_ inputPath: URL) throws -> URL {
        if inputPath.pathExtension.lowercased() == "aar" {
            return try extractClassesJar(from: inputPath)
        }
        return inputPath
    }

    /// Extracts `classes.jar` from an AAR file to a temporary directory.
    private func extractClassesJar(from aarPath: URL) throws -> URL {
        let tempDir = FileManager.default.temporaryDirectory
            .appendingPathComponent("pyjnius-wrap-aar-\(UUID().uuidString)")
        try FileManager.default.createDirectory(at: tempDir, withIntermediateDirectories: true)

        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/unzip")
        process.arguments = ["-o", aarPath.path, "classes.jar", "-d", tempDir.path]
        process.standardOutput = FileHandle.nullDevice
        process.standardError = FileHandle.nullDevice
        try process.run()
        process.waitUntilExit()

        let classesJar = tempDir.appendingPathComponent("classes.jar")
        guard FileManager.default.fileExists(atPath: classesJar.path) else {
            throw ReflectorError.noClassesJarInAar(aarPath.path)
        }
        return classesJar
    }

    /// Builds the classpath string from the target JAR and additional entries.
    private func buildClasspath(jarURL: URL, additional: [URL]) -> [String] {
        var entries = [jarURL.path]
        entries.append(contentsOf: additional.map(\.path))
        return entries
    }

    /// Enumerates all `.class` file entries in a JAR and returns their class names.
    private func enumerateClassNames(jarPath: String, environment: JNIEnvironment) throws -> [String] {
        // Use java.util.jar.JarFile to list entries.
        let jarFile = try JarFile(jarPath, environment: environment)
        var classNames: [String] = []

        let entries = jarFile.entries()
        while entries.hasMoreElements() {
            let entry = entries.nextElement()
            let name = entry.getName()
            if name.hasSuffix(".class") && !name.hasSuffix("module-info.class") {
                // Convert "com/example/Foo.class" → "com.example.Foo"
                let className = name
                    .replacingOccurrences(of: "/", with: ".")
                    .replacingOccurrences(of: ".class", with: "")
                classNames.append(className)
            }
        }
        jarFile.close()
        return classNames
    }

    /// Reflects on a single Java class and produces a `ClassNode`.
    private func reflectClass(className: String, environment: JNIEnvironment) throws -> ClassNode {
        let javaClass = try JavaClass.forName(className, environment: environment)

        let fqcn = javaClass.getName()
        let jniName = JNIDescriptor.jniName(from: fqcn)
        let simpleName = javaClass.getSimpleName()
        let kind = classKind(for: javaClass)
        let modifiers = extractModifiers(javaClass.getModifiers())
        let superclass = javaClass.getSuperclass()?.getName()
        let interfaces = javaClass.getInterfaces().map { $0.getName() }

        let fields = reflectFields(javaClass: javaClass)
        let constructors = reflectConstructors(javaClass: javaClass)
        let methods = reflectMethods(javaClass: javaClass)
        let nested = reflectNestedClasses(javaClass: javaClass, environment: environment)
        let enumConstants = reflectEnumConstants(javaClass: javaClass, kind: kind)

        return ClassNode(
            fqcn: fqcn,
            jniName: jniName,
            simpleName: simpleName,
            kind: kind,
            modifiers: modifiers,
            superclass: superclass,
            interfaces: interfaces,
            javadoc: nil, // Reflection cannot retrieve javadoc
            fields: fields,
            constructors: constructors,
            methods: methods,
            nested: nested,
            enumConstants: enumConstants
        )
    }

    /// Determines the `ClassKind` for a given Java class.
    private func classKind(for javaClass: JavaClass<JavaObject>) -> ClassKind {
        if javaClass.isAnnotation() {
            return .annotationType
        } else if javaClass.isEnum() {
            return .enumType
        } else if javaClass.isInterface() {
            return .interfaceType
        }
        return .classType
    }

    /// Extracts Java modifier flags into our `[JavaModifier]` array.
    private func extractModifiers(_ modifierBits: Int32) -> [JavaModifier] {
        var result: [JavaModifier] = []
        // java.lang.reflect.Modifier constants
        if modifierBits & 0x0001 != 0 { result.append(.public) }
        if modifierBits & 0x0002 != 0 { result.append(.private) }
        if modifierBits & 0x0004 != 0 { result.append(.protected) }
        if modifierBits & 0x0008 != 0 { result.append(.static) }
        if modifierBits & 0x0010 != 0 { result.append(.final) }
        if modifierBits & 0x0400 != 0 { result.append(.abstract) }
        return result
    }

    /// Reflects all declared fields (non-synthetic).
    private func reflectFields(javaClass: JavaClass<JavaObject>) -> [FieldNode] {
        let fields = javaClass.getDeclaredFields()
        return fields.compactMap { field -> FieldNode? in
            let mods = field.getModifiers()
            // Skip synthetic fields
            if mods & 0x1000 != 0 { return nil }

            let name = field.getName()
            let typeName = field.getType().getName()
            let jniDescriptor = JNIDescriptor.descriptor(forClassName: typeName)
            let isStatic = mods & 0x0008 != 0
            let modifiers = extractModifiers(mods)

            return FieldNode(
                name: name,
                jniDescriptor: jniDescriptor,
                typeFqcn: typeName,
                isStatic: isStatic,
                modifiers: modifiers,
                javadoc: nil
            )
        }
    }

    /// Reflects all declared constructors.
    private func reflectConstructors(javaClass: JavaClass<JavaObject>) -> [ConstructorNode] {
        let constructors = javaClass.getDeclaredConstructors()
        return constructors.compactMap { ctor -> ConstructorNode? in
            let mods = ctor.getModifiers()
            // Skip synthetic constructors
            if mods & 0x1000 != 0 { return nil }

            let paramTypes = ctor.getParameterTypes()
            let paramTypeNames = paramTypes.map { $0.getName() }
            let jniDescriptor = JNIDescriptor.methodDescriptor(
                paramTypeNames: paramTypeNames,
                returnTypeName: "void"
            )
            let isVarargs = ctor.isVarArgs()
            let modifiers = extractModifiers(mods)

            // Try to get parameter names (only available if compiled with -parameters)
            let parameters = ctor.getParameters()
            let paramNodes: [ParamNode] = zip(parameters, paramTypes).map { param, type in
                let paramName = param.getName()
                let typeName = type.getName()
                return ParamNode(
                    name: paramName,
                    jniDescriptor: JNIDescriptor.descriptor(forClassName: typeName),
                    typeFqcn: typeName
                )
            }

            return ConstructorNode(
                jniDescriptor: jniDescriptor,
                isVarargs: isVarargs,
                modifiers: modifiers,
                parameters: paramNodes,
                javadoc: nil
            )
        }
    }

    /// Reflects all declared methods (non-synthetic, non-bridge).
    private func reflectMethods(javaClass: JavaClass<JavaObject>) -> [MethodNode] {
        let methods = javaClass.getDeclaredMethods()
        return methods.compactMap { method -> MethodNode? in
            let mods = method.getModifiers()
            // Skip synthetic (0x1000) and bridge (0x0040) methods
            if mods & 0x1000 != 0 || mods & 0x0040 != 0 { return nil }

            let name = method.getName()
            let paramTypes = method.getParameterTypes()
            let paramTypeNames = paramTypes.map { $0.getName() }
            let returnTypeName = method.getReturnType().getName()
            let jniDescriptor = JNIDescriptor.methodDescriptor(
                paramTypeNames: paramTypeNames,
                returnTypeName: returnTypeName
            )
            let isStatic = mods & 0x0008 != 0
            let isVarargs = method.isVarArgs()
            let modifiers = extractModifiers(mods)

            // Check for default interface method
            var finalModifiers = modifiers
            if method.isDefault() && !finalModifiers.contains(.default) {
                finalModifiers.append(.default)
            }

            // Try to get parameter names
            let parameters = method.getParameters()
            let paramNodes: [ParamNode] = zip(parameters, paramTypes).map { param, type in
                let paramName = param.getName()
                let typeName = type.getName()
                return ParamNode(
                    name: paramName,
                    jniDescriptor: JNIDescriptor.descriptor(forClassName: typeName),
                    typeFqcn: typeName
                )
            }

            return MethodNode(
                name: name,
                jniDescriptor: jniDescriptor,
                isStatic: isStatic,
                isVarargs: isVarargs,
                modifiers: finalModifiers,
                parameters: paramNodes,
                returnTypeFqcn: returnTypeName,
                javadoc: nil
            )
        }
    }

    /// Reflects nested/inner classes declared within the given class.
    private func reflectNestedClasses(javaClass: JavaClass<JavaObject>, environment: JNIEnvironment) -> [ClassNode] {
        let declaredClasses = javaClass.getDeclaredClasses()
        return declaredClasses.compactMap { innerClass -> ClassNode? in
            let mods = innerClass.getModifiers()
            // Skip synthetic nested classes
            if mods & 0x1000 != 0 { return nil }
            // Skip anonymous classes
            let simpleName = innerClass.getSimpleName()
            if simpleName.isEmpty { return nil }

            do {
                return try reflectClass(className: innerClass.getName(), environment: environment)
            } catch {
                return nil
            }
        }
    }

    /// Reflects enum constants for enum types.
    private func reflectEnumConstants(javaClass: JavaClass<JavaObject>, kind: ClassKind) -> [EnumConstantNode]? {
        guard kind == .enumType else { return nil }

        // Enum constants are public static final fields of the enum type itself.
        let fields = javaClass.getDeclaredFields()
        let enumTypeName = javaClass.getName()

        return fields.compactMap { field -> EnumConstantNode? in
            let mods = field.getModifiers()
            // Enum constants have the ENUM flag (0x4000)
            guard mods & 0x4000 != 0 else { return nil }
            // Verify the field type matches the enum class
            guard field.getType().getName() == enumTypeName else { return nil }
            return EnumConstantNode(name: field.getName(), javadoc: nil)
        }
    }
}

// MARK: - Errors

public enum ReflectorError: Error, CustomStringConvertible {
    case noClassesJarInAar(String)
    case jvmBootFailed(String)
    case classLoadFailed(String, underlying: Error)

    public var description: String {
        switch self {
        case .noClassesJarInAar(let path):
            return "No classes.jar found in AAR: \(path)"
        case .jvmBootFailed(let msg):
            return "Failed to boot embedded JVM: \(msg)"
        case .classLoadFailed(let className, let err):
            return "Failed to load class '\(className)': \(err)"
        }
    }
}
