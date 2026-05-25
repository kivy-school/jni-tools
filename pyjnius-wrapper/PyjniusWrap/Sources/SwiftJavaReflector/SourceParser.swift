import Foundation
import PyjniusWrapCore
import SwiftJava
import JavaLangReflect

/// Parses Java source files by calling the JavaParser library directly through swift-java,
/// producing `[ClassNode]` compatible with `PyjniusWrapCore.Schema`.
///
/// This is a pure Swift implementation that calls JavaParser's API in-process via swift-java.
/// No custom Java code is required — we call JavaParser classes directly:
///
/// - `com.github.javaparser.JavaParser` for parsing `.java` source files
/// - `com.github.javaparser.symbolsolver.*` for symbol resolution
/// - AST node types for walking the parse tree
///
/// This gives us:
/// - Javadoc extraction (from source files)
/// - Proper parameter names (from source)
/// - Full symbol resolution via JavaParser's symbol solver
/// - No custom Java code — only the JavaParser JAR on the classpath
///
/// Requirements:
/// - JavaParser JAR (with dependencies) on the classpath.
/// - JDK 17+ on PATH (swift-java embeds the JVM in-process).
public struct SourceParser: Sendable {

    /// Configuration for the source parser.
    public struct Config: Sendable {
        /// Path to the directory containing `.java` source files.
        public var inputPath: URL
        /// Additional classpath entries for symbol resolution (e.g., dependent JARs).
        public var additionalClasspath: [URL]
        /// Path to a JAR containing JavaParser and its dependencies.
        /// If nil, JavaParser must already be on the JVM classpath.
        public var javaParserJarPath: URL?

        public init(inputPath: URL, additionalClasspath: [URL] = [],
                    javaParserJarPath: URL? = nil) {
            self.inputPath = inputPath
            self.additionalClasspath = additionalClasspath
            self.javaParserJarPath = javaParserJarPath
        }
    }

    public init() {}

    /// Parses all `.java` files in the configured input path and returns an `AstDocument`.
    ///
    /// Calls JavaParser's API directly in-process via swift-java. Walks the input directory,
    /// parses each `.java` file, extracts classes/interfaces/enums, and builds `ClassNode`
    /// objects in Swift — no intermediate JSON, no custom Java code.
    public func parse(config: Config) throws -> AstDocument {
        let classpath = buildClasspath(config)

        // Boot the embedded JVM with JavaParser on the classpath.
        let jvm = try JavaVirtualMachine.shared(classpath: classpath)
        let environment = try jvm.environment()

        // Find all .java files in the input directory.
        let javaFiles = try findJavaFiles(in: config.inputPath)
        if javaFiles.isEmpty {
            return AstDocument(classes: [])
        }

        // Set up JavaParser with symbol resolution.
        let parser = try createParser(sourceDir: config.inputPath, environment: environment)

        // Parse each file and extract class nodes.
        var classNodes: [ClassNode] = []
        for file in javaFiles {
            let nodes = try parseFile(file, parser: parser, environment: environment)
            classNodes.append(contentsOf: nodes)
        }

        return AstDocument(classes: classNodes)
    }

    // MARK: - Private Helpers

    private func buildClasspath(_ config: Config) -> [String] {
        var entries: [String] = []
        if let jarPath = config.javaParserJarPath {
            entries.append(jarPath.path)
        }
        entries.append(contentsOf: config.additionalClasspath.map(\.path))
        return entries
    }

    /// Recursively finds all `.java` files in a directory.
    private func findJavaFiles(in directory: URL) throws -> [URL] {
        let fm = FileManager.default
        guard let enumerator = fm.enumerator(
            at: directory,
            includingPropertiesForKeys: [.isRegularFileKey],
            options: [.skipsHiddenFiles]
        ) else {
            return []
        }
        var result: [URL] = []
        for case let url as URL in enumerator {
            if url.pathExtension == "java" {
                result.append(url)
            }
        }
        return result.sorted { $0.path < $1.path }
    }

    /// Creates a configured JavaParser instance with symbol resolution via swift-java.
    ///
    /// Equivalent to the Java code:
    /// ```java
    /// CombinedTypeSolver solver = new CombinedTypeSolver();
    /// solver.add(new ReflectionTypeSolver());
    /// solver.add(new JavaParserTypeSolver(sourceDir));
    /// ParserConfiguration config = new ParserConfiguration()
    ///     .setSymbolResolver(new JavaSymbolSolver(solver));
    /// JavaParser parser = new JavaParser(config);
    /// ```
    private func createParser(sourceDir: URL, environment: JNIEnvironment) throws -> JavaObject {
        // CombinedTypeSolver solver = new CombinedTypeSolver();
        let combinedSolverClass = try JavaClass.forName(
            "com.github.javaparser.symbolsolver.resolution.typesolvers.CombinedTypeSolver",
            environment: environment)
        let solver = try combinedSolverClass.getDeclaredConstructors()
            .first { $0.getParameterCount() == 0 }!
            .newInstance(args: [])!

        // solver.add(new ReflectionTypeSolver());
        let reflSolverClass = try JavaClass.forName(
            "com.github.javaparser.symbolsolver.resolution.typesolvers.ReflectionTypeSolver",
            environment: environment)
        let reflSolver = try reflSolverClass.getDeclaredConstructors()
            .first { $0.getParameterCount() == 0 }!
            .newInstance(args: [])!

        let addMethod = solver.getClass().getDeclaredMethods().first { m in
            m.getName() == "add" && m.getParameterCount() == 1
        }!
        try addMethod.invoke(solver, args: [reflSolver])

        // solver.add(new JavaParserTypeSolver(sourceDir));
        let jpSolverClass = try JavaClass.forName(
            "com.github.javaparser.symbolsolver.resolution.typesolvers.JavaParserTypeSolver",
            environment: environment)
        let fileClass = try JavaClass.forName("java.io.File", environment: environment)
        let file = try fileClass.getDeclaredConstructors().first { ctor in
            let params = ctor.getParameterTypes()
            return params.count == 1 && params[0].getName() == "java.lang.String"
        }!.newInstance(args: [try JavaString(sourceDir.path, environment: environment)])!

        let jpSolver = try jpSolverClass.getDeclaredConstructors().first { ctor in
            let params = ctor.getParameterTypes()
            return params.count == 1 && params[0].getName() == "java.io.File"
        }!.newInstance(args: [file])!
        try addMethod.invoke(solver, args: [jpSolver])

        // JavaSymbolSolver symbolSolver = new JavaSymbolSolver(solver);
        let symbolSolverClass = try JavaClass.forName(
            "com.github.javaparser.symbolsolver.JavaSymbolSolver",
            environment: environment)
        let symbolSolver = try symbolSolverClass.getDeclaredConstructors().first { ctor in
            ctor.getParameterCount() == 1
        }!.newInstance(args: [solver])!

        // ParserConfiguration config = new ParserConfiguration().setSymbolResolver(symbolSolver);
        let parserConfigClass = try JavaClass.forName(
            "com.github.javaparser.ParserConfiguration",
            environment: environment)
        let parserConfig = try parserConfigClass.getDeclaredConstructors()
            .first { $0.getParameterCount() == 0 }!
            .newInstance(args: [])!

        let setSymbolResolver = parserConfig.getClass().getDeclaredMethods().first { m in
            m.getName() == "setSymbolResolver" && m.getParameterCount() == 1
        }!
        try setSymbolResolver.invoke(parserConfig, args: [symbolSolver])

        // JavaParser parser = new JavaParser(config);
        let javaParserClass = try JavaClass.forName(
            "com.github.javaparser.JavaParser",
            environment: environment)
        let parser = try javaParserClass.getDeclaredConstructors().first { ctor in
            ctor.getParameterCount() == 1
        }!.newInstance(args: [parserConfig])!

        return parser
    }

    /// Parses a single `.java` file and extracts all top-level type declarations.
    private func parseFile(_ fileURL: URL, parser: JavaObject,
                           environment: JNIEnvironment) throws -> [ClassNode] {
        // File javaFile = new File(path);
        let fileClass = try JavaClass.forName("java.io.File", environment: environment)
        let javaFile = try fileClass.getDeclaredConstructors().first { ctor in
            let params = ctor.getParameterTypes()
            return params.count == 1 && params[0].getName() == "java.lang.String"
        }!.newInstance(args: [try JavaString(fileURL.path, environment: environment)])!

        // ParseResult<CompilationUnit> result = parser.parse(javaFile);
        let parseMethod = parser.getClass().getDeclaredMethods().first { m in
            m.getName() == "parse" && m.getParameterCount() == 1 &&
            m.getParameterTypes().first?.getName() == "java.io.File"
        }!
        let parseResult = try parseMethod.invoke(parser, args: [javaFile])!

        // if (!result.isSuccessful()) return [];
        let isSuccessful = parseResult.getClass().getDeclaredMethods().first { m in
            m.getName() == "isSuccessful" && m.getParameterCount() == 0
        }!
        let successObj = try isSuccessful.invoke(parseResult, args: [])
        let success = successObj?.toString() == "true"
        if !success { return [] }

        // CompilationUnit cu = result.getResult().get();
        let getResultMethod = parseResult.getClass().getDeclaredMethods().first { m in
            m.getName() == "getResult" && m.getParameterCount() == 0
        }!
        let optionalCU = try getResultMethod.invoke(parseResult, args: [])!
        let getMethod = optionalCU.getClass().getDeclaredMethods().first { m in
            m.getName() == "get" && m.getParameterCount() == 0
        }!
        let compilationUnit = try getMethod.invoke(optionalCU, args: [])!

        // Extract types from the CompilationUnit
        return try extractTypes(from: compilationUnit, environment: environment)
    }

    /// Extracts all type declarations from a CompilationUnit.
    private func extractTypes(from cu: JavaObject,
                              environment: JNIEnvironment) throws -> [ClassNode] {
        // List<TypeDeclaration<?>> types = cu.getTypes();
        let getTypes = cu.getClass().getDeclaredMethods().first { m in
            m.getName() == "getTypes" && m.getParameterCount() == 0
        }!
        let typesList = try getTypes.invoke(cu, args: [])!

        let sizeMethod = typesList.getClass().getMethod("size", parameterTypes: [])
        let size = Int(try sizeMethod.invoke(typesList, args: [])!.toString()!)!

        var classNodes: [ClassNode] = []
        let getMethod = typesList.getClass().getMethod("get", parameterTypes: [
            try JavaClass.forName("int", environment: environment)
        ])

        for i in 0..<size {
            let indexObj = try JavaInteger.valueOf(Int32(i), environment: environment)
            let typeDecl = try getMethod.invoke(typesList, args: [indexObj])!
            if let node = try extractTypeDeclaration(typeDecl, environment: environment) {
                classNodes.append(node)
            }
        }
        return classNodes
    }

    /// Extracts a single TypeDeclaration into a ClassNode.
    private func extractTypeDeclaration(_ typeDecl: JavaObject,
                                        environment: JNIEnvironment) throws -> ClassNode? {
        let className = typeDecl.getClass().getName()

        if className.contains("ClassOrInterfaceDeclaration") {
            return try extractClassOrInterface(typeDecl, environment: environment)
        } else if className.contains("EnumDeclaration") {
            return try extractEnum(typeDecl, environment: environment)
        }
        return nil
    }

    /// Extracts a ClassOrInterfaceDeclaration into a ClassNode.
    private func extractClassOrInterface(_ decl: JavaObject,
                                         environment: JNIEnvironment) throws -> ClassNode {
        // Get FQCN
        let fqcnOpt = try invokeMethod(on: decl, name: "getFullyQualifiedName", environment: environment)!
        let fqcn: String
        if let resolved = try? invokeMethod(on: fqcnOpt, name: "orElse", args: [
            try JavaString("", environment: environment)
        ], environment: environment), let str = resolved?.toString(), !str.isEmpty {
            fqcn = str
        } else {
            fqcn = try invokeMethod(on: decl, name: "getNameAsString", environment: environment)!.toString()!
        }

        let simpleName = try invokeMethod(on: decl, name: "getNameAsString", environment: environment)!.toString()!
        let isInterfaceObj = try invokeMethod(on: decl, name: "isInterface", environment: environment)!
        let isInterface = isInterfaceObj.toString() == "true"
        let kind: ClassKind = isInterface ? .interfaceType : .classType
        let jniName = fqcn.replacingOccurrences(of: ".", with: "/")

        let modifiers = try extractModifiers(from: decl, environment: environment)
        let javadoc = try extractJavadoc(from: decl, environment: environment)

        // Superclass
        let superclass = try extractSuperclass(from: decl, environment: environment)
        // Interfaces
        let interfaces = try extractImplementedInterfaces(from: decl, environment: environment)

        // Members
        let fields = try extractFields(from: decl, isInterface: isInterface, environment: environment)
        let constructors = try extractConstructors(from: decl, isInterface: isInterface, environment: environment)
        let methods = try extractMethods(from: decl, isInterface: isInterface, environment: environment)
        let nested = try extractNestedTypes(from: decl, environment: environment)

        return ClassNode(
            fqcn: fqcn,
            jniName: jniName,
            simpleName: simpleName,
            kind: kind,
            modifiers: modifiers,
            superclass: superclass,
            interfaces: interfaces,
            javadoc: javadoc,
            fields: fields,
            constructors: constructors,
            methods: methods,
            nested: nested,
            enumConstants: nil
        )
    }

    /// Extracts an EnumDeclaration into a ClassNode.
    private func extractEnum(_ decl: JavaObject,
                             environment: JNIEnvironment) throws -> ClassNode {
        let fqcnOpt = try invokeMethod(on: decl, name: "getFullyQualifiedName", environment: environment)!
        let fqcn: String
        if let resolved = try? invokeMethod(on: fqcnOpt, name: "orElse", args: [
            try JavaString("", environment: environment)
        ], environment: environment), let str = resolved?.toString(), !str.isEmpty {
            fqcn = str
        } else {
            fqcn = try invokeMethod(on: decl, name: "getNameAsString", environment: environment)!.toString()!
        }

        let simpleName = try invokeMethod(on: decl, name: "getNameAsString", environment: environment)!.toString()!
        let jniName = fqcn.replacingOccurrences(of: ".", with: "/")
        let modifiers = try extractModifiers(from: decl, environment: environment)
        let javadoc = try extractJavadoc(from: decl, environment: environment)
        let interfaces = try extractImplementedInterfaces(from: decl, environment: environment)

        // Enum constants
        let enumConstants = try extractEnumConstants(from: decl, environment: environment)

        // Enum methods
        let methods = try extractMethods(from: decl, isInterface: false, environment: environment)

        return ClassNode(
            fqcn: fqcn,
            jniName: jniName,
            simpleName: simpleName,
            kind: .enumType,
            modifiers: modifiers,
            superclass: "java.lang.Enum",
            interfaces: interfaces,
            javadoc: javadoc,
            fields: [],
            constructors: [],
            methods: methods,
            nested: [],
            enumConstants: enumConstants
        )
    }

    // MARK: - Member Extraction

    private func extractFields(from decl: JavaObject, isInterface: Bool,
                               environment: JNIEnvironment) throws -> [FieldNode] {
        let members = try getMembers(from: decl, environment: environment)
        var fields: [FieldNode] = []

        for member in members {
            let memberClass = member.getClass().getName()
            guard memberClass.contains("FieldDeclaration") else { continue }
            guard try isAccessible(member, isInterface: isInterface, environment: environment) else { continue }

            // Get variables from the field declaration
            let variables = try invokeMethod(on: member, name: "getVariables", environment: environment)!
            let varSize = Int(try invokeMethod(on: variables, name: "size", environment: environment)!.toString()!)!

            let isStatic = try checkIsStatic(member, environment: environment) || isInterface
            let fieldModifiers = try extractModifiers(from: member, environment: environment)
            let fieldJavadoc = try extractJavadoc(from: member, environment: environment)

            for vi in 0..<varSize {
                let indexObj = try JavaInteger.valueOf(Int32(vi), environment: environment)
                let variable = try invokeMethod(on: variables, name: "get", args: [indexObj], environment: environment)!

                let name = try invokeMethod(on: variable, name: "getNameAsString", environment: environment)!.toString()!
                let type = try invokeMethod(on: variable, name: "getType", environment: environment)!
                let jniDescriptor = try jniDescriptorOf(type: type, environment: environment)
                let typeFqcn = try fqcnOf(type: type, environment: environment)

                fields.append(FieldNode(
                    name: name,
                    jniDescriptor: jniDescriptor,
                    typeFqcn: typeFqcn,
                    isStatic: isStatic,
                    modifiers: fieldModifiers,
                    javadoc: fieldJavadoc
                ))
            }
        }
        return fields
    }

    private func extractConstructors(from decl: JavaObject, isInterface: Bool,
                                     environment: JNIEnvironment) throws -> [ConstructorNode] {
        let members = try getMembers(from: decl, environment: environment)
        var constructors: [ConstructorNode] = []

        for member in members {
            let memberClass = member.getClass().getName()
            guard memberClass.contains("ConstructorDeclaration") else { continue }
            guard try isAccessible(member, isInterface: isInterface, environment: environment) else { continue }

            let params = try extractParameters(from: member, environment: environment)
            let paramsDescriptor = params.map(\.jniDescriptor).joined()
            let jniDescriptor = "(\(paramsDescriptor))V"
            let isVarargs = try checkIsVarargs(member, environment: environment)
            let ctorModifiers = try extractModifiers(from: member, environment: environment)
            let ctorJavadoc = try extractJavadoc(from: member, environment: environment)

            constructors.append(ConstructorNode(
                jniDescriptor: jniDescriptor,
                isVarargs: isVarargs,
                modifiers: ctorModifiers,
                parameters: params,
                javadoc: ctorJavadoc
            ))
        }
        return constructors
    }

    private func extractMethods(from decl: JavaObject, isInterface: Bool,
                                environment: JNIEnvironment) throws -> [MethodNode] {
        let members = try getMembers(from: decl, environment: environment)
        var methods: [MethodNode] = []

        for member in members {
            let memberClass = member.getClass().getName()
            guard memberClass.contains("MethodDeclaration") else { continue }
            guard try isAccessible(member, isInterface: isInterface, environment: environment) else { continue }

            let name = try invokeMethod(on: member, name: "getNameAsString", environment: environment)!.toString()!
            let params = try extractParameters(from: member, environment: environment)
            let returnType = try invokeMethod(on: member, name: "getType", environment: environment)!
            let returnDescriptor = try jniDescriptorOf(type: returnType, environment: environment)
            let returnFqcn = try fqcnOf(type: returnType, environment: environment)
            let paramsDescriptor = params.map(\.jniDescriptor).joined()
            let jniDescriptor = "(\(paramsDescriptor))\(returnDescriptor)"
            let isStatic = try checkIsStatic(member, environment: environment)
            let isVarargs = try checkIsVarargs(member, environment: environment)
            let methodModifiers = try extractModifiers(from: member, environment: environment)
            let methodJavadoc = try extractJavadoc(from: member, environment: environment)

            methods.append(MethodNode(
                name: name,
                jniDescriptor: jniDescriptor,
                isStatic: isStatic,
                isVarargs: isVarargs,
                modifiers: methodModifiers,
                parameters: params,
                returnTypeFqcn: returnFqcn,
                javadoc: methodJavadoc
            ))
        }
        return methods
    }

    private func extractNestedTypes(from decl: JavaObject,
                                    environment: JNIEnvironment) throws -> [ClassNode] {
        let members = try getMembers(from: decl, environment: environment)
        var nested: [ClassNode] = []

        for member in members {
            let memberClass = member.getClass().getName()
            if memberClass.contains("ClassOrInterfaceDeclaration") ||
               memberClass.contains("EnumDeclaration") {
                if let node = try extractTypeDeclaration(member, environment: environment) {
                    nested.append(node)
                }
            }
        }
        return nested
    }

    private func extractEnumConstants(from decl: JavaObject,
                                      environment: JNIEnvironment) throws -> [EnumConstantNode] {
        let getEntries = decl.getClass().getDeclaredMethods().first { m in
            m.getName() == "getEntries" && m.getParameterCount() == 0
        }!
        let entries = try getEntries.invoke(decl, args: [])!

        let size = Int(try invokeMethod(on: entries, name: "size", environment: environment)!.toString()!)!
        var constants: [EnumConstantNode] = []

        for i in 0..<size {
            let indexObj = try JavaInteger.valueOf(Int32(i), environment: environment)
            let entry = try invokeMethod(on: entries, name: "get", args: [indexObj], environment: environment)!
            let name = try invokeMethod(on: entry, name: "getNameAsString", environment: environment)!.toString()!
            let javadoc = try extractJavadoc(from: entry, environment: environment)
            constants.append(EnumConstantNode(name: name, javadoc: javadoc))
        }
        return constants
    }

    // MARK: - Parameter Extraction

    private func extractParameters(from callable: JavaObject,
                                   environment: JNIEnvironment) throws -> [ParamNode] {
        let getParams = callable.getClass().getDeclaredMethods().first { m in
            m.getName() == "getParameters" && m.getParameterCount() == 0
        }!
        let paramsList = try getParams.invoke(callable, args: [])!
        let size = Int(try invokeMethod(on: paramsList, name: "size", environment: environment)!.toString()!)!

        var params: [ParamNode] = []
        for i in 0..<size {
            let indexObj = try JavaInteger.valueOf(Int32(i), environment: environment)
            let param = try invokeMethod(on: paramsList, name: "get", args: [indexObj], environment: environment)!

            let name = try invokeMethod(on: param, name: "getNameAsString", environment: environment)!.toString()!
            let type = try invokeMethod(on: param, name: "getType", environment: environment)!
            let isVarArgsObj = try invokeMethod(on: param, name: "isVarArgs", environment: environment)!
            let isVarArgs = isVarArgsObj.toString() == "true"

            var jniDescriptor = try jniDescriptorOf(type: type, environment: environment)
            var typeFqcn = try fqcnOf(type: type, environment: environment)

            if isVarArgs {
                jniDescriptor = "[" + jniDescriptor
                typeFqcn = typeFqcn + "[]"
            }

            params.append(ParamNode(
                name: name,
                jniDescriptor: jniDescriptor,
                typeFqcn: typeFqcn
            ))
        }
        return params
    }

    // MARK: - JNI Descriptor Generation (mirrors JniDescriptor.java logic)

    /// Generates a JNI type descriptor from a JavaParser Type AST node.
    /// Equivalent to `JniDescriptor.of(Type)` in the removed Java code.
    private func jniDescriptorOf(type: JavaObject,
                                 environment: JNIEnvironment) throws -> String {
        let typeName = type.getClass().getName()

        if typeName.contains("VoidType") {
            return "V"
        }
        if typeName.contains("PrimitiveType") {
            let primitiveStr = try invokeMethod(on: type, name: "getType", environment: environment)!.toString()!
            return primitiveDescriptor(primitiveStr)
        }
        if typeName.contains("ArrayType") {
            let componentType = try invokeMethod(on: type, name: "getComponentType", environment: environment)!
            return "[" + (try jniDescriptorOf(type: componentType, environment: environment))
        }

        // Try symbol resolution for fully-qualified reference types.
        do {
            let resolved = try invokeMethod(on: type, name: "resolve", environment: environment)!
            return try jniDescriptorOfResolved(resolved: resolved, environment: environment)
        } catch {
            // Fallback for unresolved ClassOrInterfaceType
            if typeName.contains("ClassOrInterfaceType") {
                let nameWithScope = try invokeMethod(on: type, name: "getNameWithScope", environment: environment)!.toString()!
                let fqcn = fqcnFallback(nameWithScope)
                return "L\(fqcn.replacingOccurrences(of: ".", with: "/"));"
            }
            return "Ljava/lang/Object;"
        }
    }

    /// Generates a JNI descriptor from a resolved type.
    private func jniDescriptorOfResolved(resolved: JavaObject,
                                         environment: JNIEnvironment) throws -> String {
        let isVoidObj = try invokeMethod(on: resolved, name: "isVoid", environment: environment)
        if isVoidObj?.toString() == "true" { return "V" }

        let isPrimObj = try invokeMethod(on: resolved, name: "isPrimitive", environment: environment)
        if isPrimObj?.toString() == "true" {
            let prim = try invokeMethod(on: resolved, name: "asPrimitive", environment: environment)!
            let desc = prim.toString()!
            return primitiveDescriptor(desc)
        }

        let isArrayObj = try invokeMethod(on: resolved, name: "isArray", environment: environment)
        if isArrayObj?.toString() == "true" {
            let asArray = try invokeMethod(on: resolved, name: "asArrayType", environment: environment)!
            let component = try invokeMethod(on: asArray, name: "getComponentType", environment: environment)!
            return "[" + (try jniDescriptorOfResolved(resolved: component, environment: environment))
        }

        let isRefObj = try invokeMethod(on: resolved, name: "isReferenceType", environment: environment)
        if isRefObj?.toString() == "true" {
            let asRef = try invokeMethod(on: resolved, name: "asReferenceType", environment: environment)!
            let qualifiedName = try invokeMethod(on: asRef, name: "getQualifiedName", environment: environment)!.toString()!
            return "L\(qualifiedName.replacingOccurrences(of: ".", with: "/"));"
        }

        // Type variable (generic erasure) → java.lang.Object
        return "Ljava/lang/Object;"
    }

    /// Gets the FQCN for a JavaParser Type AST node.
    private func fqcnOf(type: JavaObject, environment: JNIEnvironment) throws -> String {
        let typeName = type.getClass().getName()

        if typeName.contains("VoidType") { return "void" }
        if typeName.contains("PrimitiveType") {
            let prim = try invokeMethod(on: type, name: "getType", environment: environment)!
            return try invokeMethod(on: prim, name: "asString", environment: environment)!.toString()!
        }
        if typeName.contains("ArrayType") {
            let comp = try invokeMethod(on: type, name: "getComponentType", environment: environment)!
            return try fqcnOf(type: comp, environment: environment) + "[]"
        }

        // Try symbol resolution
        do {
            let resolved = try invokeMethod(on: type, name: "resolve", environment: environment)!
            return try fqcnOfResolved(resolved: resolved, environment: environment)
        } catch {
            if typeName.contains("ClassOrInterfaceType") {
                let nameWithScope = try invokeMethod(on: type, name: "getNameWithScope", environment: environment)!.toString()!
                return fqcnFallback(nameWithScope)
            }
            return "java.lang.Object"
        }
    }

    private func fqcnOfResolved(resolved: JavaObject, environment: JNIEnvironment) throws -> String {
        let isVoidObj = try invokeMethod(on: resolved, name: "isVoid", environment: environment)
        if isVoidObj?.toString() == "true" { return "void" }

        let isPrimObj = try invokeMethod(on: resolved, name: "isPrimitive", environment: environment)
        if isPrimObj?.toString() == "true" {
            let prim = try invokeMethod(on: resolved, name: "asPrimitive", environment: environment)!
            let desc = try invokeMethod(on: prim, name: "describe", environment: environment)!.toString()!
            return desc
        }

        let isArrayObj = try invokeMethod(on: resolved, name: "isArray", environment: environment)
        if isArrayObj?.toString() == "true" {
            let asArray = try invokeMethod(on: resolved, name: "asArrayType", environment: environment)!
            let comp = try invokeMethod(on: asArray, name: "getComponentType", environment: environment)!
            return try fqcnOfResolved(resolved: comp, environment: environment) + "[]"
        }

        let isRefObj = try invokeMethod(on: resolved, name: "isReferenceType", environment: environment)
        if isRefObj?.toString() == "true" {
            let asRef = try invokeMethod(on: resolved, name: "asReferenceType", environment: environment)!
            return try invokeMethod(on: asRef, name: "getQualifiedName", environment: environment)!.toString()!
        }

        return "java.lang.Object"
    }

    // MARK: - Modifier & Javadoc Extraction

    private func extractModifiers(from node: JavaObject,
                                  environment: JNIEnvironment) throws -> [JavaModifier] {
        var result: [JavaModifier] = []
        let modifierChecks: [(String, JavaModifier)] = [
            ("PUBLIC", .public),
            ("PROTECTED", .protected),
            ("PRIVATE", .private),
            ("STATIC", .static),
            ("FINAL", .final),
            ("ABSTRACT", .abstract),
            ("DEFAULT", .default),
        ]

        for (keyword, modifier) in modifierChecks {
            if try hasModifier(node, keyword: keyword, environment: environment) {
                result.append(modifier)
            }
        }
        return result
    }

    private func hasModifier(_ node: JavaObject, keyword: String,
                             environment: JNIEnvironment) throws -> Bool {
        // node.hasModifier(Modifier.Keyword.PUBLIC) etc.
        let hasModMethod = node.getClass().getMethods().first { m in
            m.getName() == "hasModifier" && m.getParameterCount() == 1
        }
        guard let hasModMethod else { return false }

        let keywordClass = try JavaClass.forName(
            "com.github.javaparser.ast.Modifier$Keyword", environment: environment)
        let valueOfMethod = keywordClass.getDeclaredMethods().first { m in
            m.getName() == "valueOf" && m.getParameterCount() == 1
        }!
        let keywordEnum = try valueOfMethod.invoke(nil, args: [
            try JavaString(keyword, environment: environment)
        ])!

        let result = try hasModMethod.invoke(node, args: [keywordEnum])
        return result?.toString() == "true"
    }

    private func extractJavadoc(from node: JavaObject,
                                environment: JNIEnvironment) throws -> String? {
        let getJavadocMethod = node.getClass().getMethods().first { m in
            m.getName() == "getJavadoc" && m.getParameterCount() == 0
        }
        guard let getJavadocMethod else { return nil }

        let optJavadoc = try getJavadocMethod.invoke(node, args: [])!
        let isPresentMethod = optJavadoc.getClass().getDeclaredMethods().first { m in
            m.getName() == "isPresent" && m.getParameterCount() == 0
        }!
        let isPresent = try isPresentMethod.invoke(optJavadoc, args: [])?.toString() == "true"
        guard isPresent else { return nil }

        let getMethod = optJavadoc.getClass().getDeclaredMethods().first { m in
            m.getName() == "get" && m.getParameterCount() == 0
        }!
        let javadoc = try getMethod.invoke(optJavadoc, args: [])!
        let getDesc = javadoc.getClass().getDeclaredMethods().first { m in
            m.getName() == "getDescription" && m.getParameterCount() == 0
        }!
        let description = try getDesc.invoke(javadoc, args: [])!
        let toText = description.getClass().getDeclaredMethods().first { m in
            m.getName() == "toText" && m.getParameterCount() == 0
        }!
        let text = try toText.invoke(description, args: [])?.toString()?.trimmingCharacters(in: .whitespacesAndNewlines)
        return text?.isEmpty == true ? nil : text
    }

    // MARK: - Superclass & Interfaces

    private func extractSuperclass(from decl: JavaObject,
                                   environment: JNIEnvironment) throws -> String? {
        let getExtended = decl.getClass().getDeclaredMethods().first { m in
            m.getName() == "getExtendedTypes" && m.getParameterCount() == 0
        }!
        let extendedTypes = try getExtended.invoke(decl, args: [])!
        let isEmpty = try invokeMethod(on: extendedTypes, name: "isEmpty", environment: environment)!
        if isEmpty.toString() == "true" { return nil }

        let indexObj = try JavaInteger.valueOf(0, environment: environment)
        let firstType = try invokeMethod(on: extendedTypes, name: "get", args: [indexObj], environment: environment)!
        return try fqcnOf(type: firstType, environment: environment)
    }

    private func extractImplementedInterfaces(from decl: JavaObject,
                                              environment: JNIEnvironment) throws -> [String] {
        let getImplemented = decl.getClass().getDeclaredMethods().first { m in
            m.getName() == "getImplementedTypes" && m.getParameterCount() == 0
        }!
        let implTypes = try getImplemented.invoke(decl, args: [])!
        let size = Int(try invokeMethod(on: implTypes, name: "size", environment: environment)!.toString()!)!

        var interfaces: [String] = []
        for i in 0..<size {
            let indexObj = try JavaInteger.valueOf(Int32(i), environment: environment)
            let implType = try invokeMethod(on: implTypes, name: "get", args: [indexObj], environment: environment)!
            interfaces.append(try fqcnOf(type: implType, environment: environment))
        }
        return interfaces
    }

    // MARK: - Utility Helpers

    private func getMembers(from decl: JavaObject,
                            environment: JNIEnvironment) throws -> [JavaObject] {
        let getMembers = decl.getClass().getDeclaredMethods().first { m in
            m.getName() == "getMembers" && m.getParameterCount() == 0
        }!
        let membersList = try getMembers.invoke(decl, args: [])!
        let size = Int(try invokeMethod(on: membersList, name: "size", environment: environment)!.toString()!)!

        var members: [JavaObject] = []
        for i in 0..<size {
            let indexObj = try JavaInteger.valueOf(Int32(i), environment: environment)
            let member = try invokeMethod(on: membersList, name: "get", args: [indexObj], environment: environment)!
            members.append(member)
        }
        return members
    }

    private func isAccessible(_ node: JavaObject, isInterface: Bool,
                              environment: JNIEnvironment) throws -> Bool {
        let hasPublic = try hasModifier(node, keyword: "PUBLIC", environment: environment)
        let hasProtected = try hasModifier(node, keyword: "PROTECTED", environment: environment)
        if hasPublic || hasProtected { return true }
        if !isInterface { return false }
        // Interface members without explicit visibility are implicitly public
        let hasPrivate = try hasModifier(node, keyword: "PRIVATE", environment: environment)
        return !hasPrivate
    }

    private func checkIsStatic(_ node: JavaObject, environment: JNIEnvironment) throws -> Bool {
        let isStaticMethod = node.getClass().getMethods().first { m in
            m.getName() == "isStatic" && m.getParameterCount() == 0
        }
        guard let isStaticMethod else { return false }
        let result = try isStaticMethod.invoke(node, args: [])
        return result?.toString() == "true"
    }

    private func checkIsVarargs(_ node: JavaObject, environment: JNIEnvironment) throws -> Bool {
        // Check last parameter for varargs
        let getParams = node.getClass().getDeclaredMethods().first { m in
            m.getName() == "getParameters" && m.getParameterCount() == 0
        }
        guard let getParams else { return false }
        let paramsList = try getParams.invoke(node, args: [])!
        let isEmpty = try invokeMethod(on: paramsList, name: "isEmpty", environment: environment)!
        if isEmpty.toString() == "true" { return false }

        let size = Int(try invokeMethod(on: paramsList, name: "size", environment: environment)!.toString()!)!
        let lastIdx = try JavaInteger.valueOf(Int32(size - 1), environment: environment)
        let lastParam = try invokeMethod(on: paramsList, name: "get", args: [lastIdx], environment: environment)!
        let isVarArgsObj = try invokeMethod(on: lastParam, name: "isVarArgs", environment: environment)!
        return isVarArgsObj.toString() == "true"
    }

    /// General-purpose method invocation helper.
    private func invokeMethod(on obj: JavaObject, name: String,
                              args: [JavaObject] = [],
                              environment: JNIEnvironment) throws -> JavaObject? {
        let methods = obj.getClass().getMethods()
        let method = methods.first { m in
            m.getName() == name && m.getParameterCount() == Int32(args.count)
        }
        guard let method else {
            throw SourceParserError.parseError("Method '\(name)' not found on \(obj.getClass().getName())")
        }
        return try method.invoke(obj, args: args)
    }

    // MARK: - Primitive & Fallback Maps

    private func primitiveDescriptor(_ primitive: String) -> String {
        let upper = primitive.uppercased()
        switch upper {
        case "BOOLEAN": return "Z"
        case "BYTE":    return "B"
        case "CHAR":    return "C"
        case "SHORT":   return "S"
        case "INT":     return "I"
        case "LONG":    return "J"
        case "FLOAT":   return "F"
        case "DOUBLE":  return "D"
        default:        return "I" // fallback
        }
    }

    private func fqcnFallback(_ written: String) -> String {
        if written.contains(".") { return written }
        switch written {
        case "String", "Object", "Integer", "Long", "Short", "Byte",
             "Float", "Double", "Boolean", "Character", "Number",
             "CharSequence", "Throwable", "Exception",
             "RuntimeException", "Class", "Iterable":
            return "java.lang.\(written)"
        default:
            return written
        }
    }
}

// MARK: - Errors

public enum SourceParserError: Error, CustomStringConvertible {
    case parseError(String)
    case symbolResolutionFailed(String)

    public var description: String {
        switch self {
        case .parseError(let msg):
            return "Source parser error: \(msg)"
        case .symbolResolutionFailed(let msg):
            return "Symbol resolution failed: \(msg)"
        }
    }
}

