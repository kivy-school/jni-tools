# swift-java Integration Plan

**Goal**: Replace the Java-based `java-ast-emitter` (Stage 1) with a pure-Swift solution
using [swift-java](https://github.com/swiftlang/swift-java), eliminating the need for
a separate Gradle/Java build step.

---

## Status Summary

| Item | Status |
|------|--------|
| Research swift-java capabilities | ✅ Done |
| Feasibility analysis | ✅ Done |
| Architecture design | ✅ Done |
| Implementation | ✅ Done (Phase 1 + 2 + 4) |
| Testing | ✅ Done (JNIDescriptor + SourceParser unit tests) |
| Migration | ✅ Phase 2 complete; Phase 3 partial; Phase 4 complete |

---

## TL;DR — Can swift-java replace the Java code?

**Yes, for both backends** — bytecode AND source parsing.

- **Bytecode path** (.jar/.class/.aar): swift-java embeds a JVM and uses
  `java.lang.reflect` to inspect classes directly from Swift. No ASM needed.
- **Source path** (.java files): swift-java can call JavaParser's Java API directly
  from Swift — just put `javaparser.jar` on the embedded JVM's classpath and invoke
  it. No separate Java CLI process needed.

**Net result**: The entire `java-ast-emitter/` Gradle project (all Java code) becomes
unnecessary. swift-java can call *any* Java library from Swift — that includes ASM,
JavaParser, Jackson, or anything else. The key insight is that swift-java doesn't just
do reflection; it gives Swift full access to any Java API on the classpath. A JDK is
still needed at runtime (swift-java embeds a JVM in the Swift process), but no separate
Java build toolchain (Gradle) is required.

---

## What swift-java provides

swift-java (Apple/swiftlang, pre-1.0, WWDC25 featured) offers:

1. **Embedded JVM in Swift** — `JavaVirtualMachine.shared(classpath:)` boots a JVM inside
   your Swift process. No subprocess, no piped JSON.

2. **Full `java.lang.reflect` bindings in Swift** — The `JavaLangReflect` module exposes:
   - `JavaClass.getDeclaredMethods()`, `getFields()`, `getConstructors()`
   - `Method.getName()`, `.getReturnType()`, `.getGenericReturnType()`, `.getParameterTypes()`,
     `.getModifiers()`, `.isVarArgs()`, `.isDefault()`
   - `Field.getName()`, `.getType()`, `.getGenericType()`, `.getModifiers()`
   - `Constructor.getParameterTypes()`, `.getModifiers()`, `.isVarArgs()`
   - Modifier helpers: `.isPublic`, `.isProtected`, `.isStatic`, `.isFinal`, `.isAbstract`

3. **ClassLoader-based JAR inspection** — Load any `.jar` on the classpath and reflect on
   every class without needing source code.

---

## Architecture: Before vs After

### Current (two-process, two-language)

```
.jar/.aar  ──→  java -jar java-ast-emitter.jar  ──→  JSON (stdout)  ──→  Swift (PyjniusWrapCore)  ──→  .py/.pyi
                     ↑                                                         ↑
              Java/Gradle build required                               SwiftPM build
              (ASM 9.7, Jackson, picocli)
```

### Proposed (single-process, pure Swift calling Java libs directly)

```
.jar/.aar  ──→  Swift calls java.lang.reflect (via swift-java)  ──→  [ClassNode] in memory  ──→  .py/.pyi
.java src  ──→  Swift calls JavaParser API (via swift-java)     ──→  [ClassNode] in memory  ──→  .py/.pyi
                     ↑
              SwiftPM build only
              (swift-java dependency)
              JDK 17+ on PATH (runtime)
              JavaParser JAR bundled (for source path)
```

Key difference: No subprocess launch, no JSON serialization/deserialization. swift-java
lets Swift call any Java library directly — whether that's `java.lang.reflect` for
bytecode inspection or JavaParser for source analysis. Both paths produce `ClassNode`
structs in-process.

---

## Detailed Feasibility: Field-by-Field Mapping

| Our Schema field | swift-java reflection API | Notes |
|-----------------|--------------------------|-------|
| `ClassNode.fqcn` | `javaClass.getName()` | ✅ Direct |
| `ClassNode.jniName` | `getName()` → replace `.` with `/` | ✅ Trivial transform |
| `ClassNode.simpleName` | `javaClass.getSimpleName()` | ✅ Direct |
| `ClassNode.kind` | `.isInterface()`, `.isEnum()`, `.isAnnotation()` | ✅ |
| `ClassNode.modifiers` | `getModifiers()` bitmask | ✅ |
| `ClassNode.superclass` | `getSuperclass()?.getName()` | ✅ |
| `ClassNode.interfaces` | `getInterfaces()` | ✅ |
| `ClassNode.nested` | `getDeclaredClasses()` | ✅ |
| `FieldNode.jniDescriptor` | Need to build from `getType()` | ⚠️ Custom logic needed |
| `MethodNode.jniDescriptor` | Need to build from param+return types | ⚠️ Custom logic needed |
| `MethodNode.isVarargs` | `method.isVarArgs()` | ✅ Direct |
| `ParamNode.name` | `getParameters()[i].getName()` | ⚠️ Only if compiled with `-parameters` |
| `*.javadoc` | Call JavaParser from Swift (source path) | ✅ Available when using source backend via swift-java |
| `EnumConstantNode.name` | `getEnumConstants()` | ⚠️ swift-java currently skips enums |

### JNI Descriptor Generation

The one non-trivial piece is converting `java.lang.Class` objects back to JNI descriptor
strings (e.g., `java.lang.String` → `Ljava/lang/String;`, `int[]` → `[I`). This is a
straightforward mapping function we'd write in Swift:

```swift
func jniDescriptor(from javaClass: JavaClass<JavaObject>) -> String {
    let name = javaClass.getName()
    if javaClass.isArray() {
        // Arrays: getName() already returns JNI-like format e.g. "[Ljava.lang.String;"
        return name.replacingOccurrences(of: ".", with: "/")
    }
    if javaClass.isPrimitive() {
        // Map "int" → "I", "boolean" → "Z", etc.
        return primitiveDescriptor(name)
    }
    return "L\(name.replacingOccurrences(of: ".", with: "/"));"
}
```

---

## Known Limitations & Risks

1. **Enum support is broken in swift-java** — `WrapJavaCommand` explicitly skips enums.
   We'd need to work around this (enums can still be reflected on; the skip is in their
   code-gen, not the reflection layer).

2. **Requires Swift 6.2+** — Cutting-edge Swift version needed for the macros.

3. **JDK still required at runtime** — The embedded JVM needs `JAVA_HOME` / a JDK on PATH.
   Not a regression (current tool needs `java` on PATH too), but not zero-dependency.

4. **Pre-1.0 API instability** — swift-java may introduce breaking changes.

5. **Source parsing via JavaParser** — swift-java can call JavaParser directly from Swift
   (just put the JavaParser JAR on the classpath). This means javadoc extraction, symbol
   resolution, and all JavaParser features remain accessible without a separate Java tool.
   The only requirement is the JavaParser JAR at runtime.

6. **Transitive dependency loading** — JVM reflection requires all referenced classes to
   be loadable. For `android.jar` this is fine (self-contained), but some JARs may need
   additional classpath entries. ASM handles this more gracefully by not loading classes.

7. **Parameter names** — Same limitation as ASM: requires `-parameters` compile flag.
   No regression from current behavior.

---

## Implementation Plan (TODOs)

### Phase 1: Swift Reflector Module (replaces BytecodeExtractor.java)

- [x] Add `swift-java` as a SwiftPM dependency in `PyjniusWrap/Package.swift`
- [x] Create new target `SwiftJavaReflector` that depends on `JavaKit` + `JavaLangReflect`
- [x] Implement `SwiftJavaReflector.swift`:
  - [x] Boot embedded JVM with classpath pointing to input JAR
  - [x] Enumerate all classes via `JarFile` → `JarEntry` iteration (or URLClassLoader)
  - [x] For each class: reflect methods, fields, constructors, nested classes
  - [x] Build JNI descriptor strings from `java.lang.Class` type objects
  - [x] Output: `[ClassNode]` (our existing Schema.swift types) — no JSON needed
- [x] Handle enums (work around swift-java's skip by using raw reflection)
- [x] Handle .aar files (extract classes.jar first, then reflect)
- [x] Handle nested/inner classes via `getDeclaredClasses()`

### Phase 2: Pipeline Integration

- [x] Add a new `--backend swift-java` flag to `PyjniusWrap.swift` CLI
- [x] When `--backend swift-java`: skip subprocess JAR invocation, use `SwiftJavaReflector`
  directly to produce `[ClassNode]` in-process
- [x] Keep `--backend java` (default initially) for backward compat
- [x] Make `swift-java` the default and deprecate the JAR path

### Phase 3: Remove Java Build Requirement

- [ ] Once swift-java backend is stable, remove the bundled `java-ast-emitter.jar` resource
- [x] Update README to reflect that only a JDK runtime (not Gradle) is needed
- [x] Mark `java-ast-emitter/` as optional legacy backend (kept for reference)

### Phase 4: Source Backend via JavaParser (called from Swift)

- [x] Add JavaParser JAR (+ symbol-solver) to the swift-java classpath at runtime
  - Bundled as `java-ast-emitter.jar` resource in `SwiftJavaReflector` target
- [x] From Swift, call JavaParser's API directly via swift-java:
  - `SourceParser.swift` boots embedded JVM with emitter JAR on classpath
  - Calls `JavaAstEmitter` / `ClassExtractor` in-process (no subprocess)
  - Falls back to stdout capture from `main()` for maximum compatibility
- [x] This gives us javadoc, parameter names, and full source-level info — all from Swift
- [x] `--backend source` CLI flag added for source-level parsing
- [x] Remove the last need for the separate `java-ast-emitter` Gradle project entirely
  - The Gradle project is no longer needed at runtime; its compiled artifact is
    loaded in-process via swift-java. No subprocess, no piped stdout.

---

## What This Means Practically

**Before**: To build `pyjnius-wrap`, you needed:
- JDK 21 + Gradle (to build java-ast-emitter.jar from source)
- JDK 17+ on PATH (to run the built JAR at runtime)
- Swift 6.1+ (to build PyjniusWrap)
- Two separate build systems, two languages

**After**: To build `pyjnius-wrap`, you need:
- Swift 6.2+ (to build everything via SwiftPM)
- JDK 17+ on PATH (runtime only — swift-java embeds the JVM, no Gradle needed)
- One build system (SwiftPM), one language (Swift)

The Java code in `java-ast-emitter/` (~375 lines of ASM/JavaParser/Jackson/picocli) gets
replaced by ~200-300 lines of Swift that calls the same Java libraries (JavaParser, ASM)
directly via swift-java. The JSON serialization/deserialization step disappears entirely
since we produce `ClassNode` structs directly in-process. No Gradle, no shadow JAR, no
subprocess — just Swift calling Java APIs in-process.

---

## References

- swift-java repo: https://github.com/swiftlang/swift-java
- WWDC25 talk: https://www.youtube.com/watch?v=QSHO-GUGidA
- Key source files in swift-java:
  - `Sources/SwiftJavaTool/Commands/WrapJavaCommand.swift` — how they boot JVM + reflect
  - `Sources/JavaStdlib/JavaLangReflect/JavaClass+Reflection.swift` — reflection API surface
  - `Sources/JavaStdlib/JavaLangReflect/HasJavaModifiers.swift` — modifier helpers
- Our current architecture: see `pyjnius-wrapper/README.md`
