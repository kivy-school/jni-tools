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
| Implementation | ❌ TODO |
| Testing | ❌ TODO |
| Migration | ❌ TODO |

---

## TL;DR — Can swift-java replace the Java code?

**Yes, for the bytecode (.jar/.class/.aar) backend** — which is the most important one
(it's what wraps closed-source SDKs like AdMob, android.jar, Firebase, etc.).

**No, for the .java source parsing backend** — swift-java uses live JVM reflection which
requires compiled bytecode. JavaParser-style source analysis cannot be replicated.

**Net result**: For the primary use case (wrapping compiled JARs/AARs), swift-java lets us
do everything in Swift. The Gradle project and all its Java code (`BytecodeExtractor.java`,
`AstDtos.java`, `JniDescriptor.java`, etc.) become unnecessary for that path. A JDK is
still needed at runtime (swift-java embeds a JVM in the Swift process), but no separate
Java build toolchain is required.

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

### Proposed (single-process, pure Swift)

```
.jar/.aar  ──→  Swift (SwiftJavaReflector)  ──→  [ClassNode] in memory  ──→  Swift (PyjniusWrapCore)  ──→  .py/.pyi
                     ↑                                                            ↑
              SwiftPM build only                                           Same as today
              (swift-java dependency)
              JDK 17+ on PATH (runtime)
```

Key difference: No subprocess launch, no JSON serialization/deserialization for the
bytecode path. The reflection data flows directly into our existing `Schema.swift`
(`ClassNode`, `MethodNode`, `FieldNode`) structs.

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
| `*.javadoc` | Not available via reflection | ❌ Same limitation as ASM |
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

5. **No .java source parsing** — If users rely on the JavaParser source backend for
   javadoc extraction or compiling-from-source workflows, that path must remain as a
   fallback (or be dropped as a feature).

6. **Transitive dependency loading** — JVM reflection requires all referenced classes to
   be loadable. For `android.jar` this is fine (self-contained), but some JARs may need
   additional classpath entries. ASM handles this more gracefully by not loading classes.

7. **Parameter names** — Same limitation as ASM: requires `-parameters` compile flag.
   No regression from current behavior.

---

## Implementation Plan (TODOs)

### Phase 1: Swift Reflector Module (replaces BytecodeExtractor.java)

- [ ] Add `swift-java` as a SwiftPM dependency in `PyjniusWrap/Package.swift`
- [ ] Create new target `SwiftJavaReflector` that depends on `JavaKit` + `JavaLangReflect`
- [ ] Implement `SwiftJavaReflector.swift`:
  - [ ] Boot embedded JVM with classpath pointing to input JAR
  - [ ] Enumerate all classes via `JarFile` → `JarEntry` iteration (or URLClassLoader)
  - [ ] For each class: reflect methods, fields, constructors, nested classes
  - [ ] Build JNI descriptor strings from `java.lang.Class` type objects
  - [ ] Output: `[ClassNode]` (our existing Schema.swift types) — no JSON needed
- [ ] Handle enums (work around swift-java's skip by using raw reflection)
- [ ] Handle .aar files (extract classes.jar first, then reflect)
- [ ] Handle nested/inner classes via `getDeclaredClasses()`

### Phase 2: Pipeline Integration

- [ ] Add a new `--backend swift-java` flag to `PyjniusWrap.swift` CLI
- [ ] When `--backend swift-java`: skip subprocess JAR invocation, use `SwiftJavaReflector`
  directly to produce `[ClassNode]` in-process
- [ ] Keep `--backend java` (default initially) for backward compat
- [ ] Eventually make `swift-java` the default and deprecate the JAR path

### Phase 3: Remove Java Build Requirement

- [ ] Once swift-java backend is stable, remove the bundled `java-ast-emitter.jar` resource
- [ ] Update README to reflect that only a JDK runtime (not Gradle) is needed
- [ ] Keep `java-ast-emitter/` source for reference or as an optional advanced backend

### Phase 4: Source Backend (Optional/Future)

- [ ] If .java source parsing is still needed, keep the JAR-based JavaParser path as a
  legacy option
- [ ] Alternatively, investigate whether swift-java could compile sources on-the-fly
  using `javax.tools.JavaCompiler` (available via reflection) and then reflect on them

---

## What This Means Practically

**Before**: To build `pyjnius-wrap`, you needed:
- JDK 21 + Gradle (to build java-ast-emitter.jar)
- Swift 6.1+ (to build PyjniusWrap)
- Two separate build systems, two languages

**After**: To build `pyjnius-wrap`, you need:
- Swift 6.2+ (to build everything)
- JDK 17+ on PATH (runtime only, no Gradle needed)
- One build system (SwiftPM), one language (Swift)

The Java code in `java-ast-emitter/` (~375 lines of ASM/JavaParser/Jackson/picocli) gets
replaced by ~200-300 lines of Swift using swift-java's reflection APIs. The JSON
serialization/deserialization step disappears entirely since we produce `ClassNode` structs
directly in-process.

---

## References

- swift-java repo: https://github.com/swiftlang/swift-java
- WWDC25 talk: https://www.youtube.com/watch?v=QSHO-GUGidA
- Key source files in swift-java:
  - `Sources/SwiftJavaTool/Commands/WrapJavaCommand.swift` — how they boot JVM + reflect
  - `Sources/JavaStdlib/JavaLangReflect/JavaClass+Reflection.swift` — reflection API surface
  - `Sources/JavaStdlib/JavaLangReflect/HasJavaModifiers.swift` — modifier helpers
- Our current architecture: see `pyjnius-wrapper/README.md`
