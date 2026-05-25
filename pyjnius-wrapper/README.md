# pyjnius-wrap

CLI tool that auto-generates [pyjnius](https://github.com/kivy/pyjnius) Python
wrapper modules from Java source files.

## Pipeline

```
    .java sources    ──┐
                       │
    .jar / .aar / .class ──┤  (compiled artifacts, no source needed)
                       │
                       ▼
   java-ast-emitter.jar     (JavaParser OR ASM bytecode, JDK 17+)
      ─── OR ───
   swift-java reflector     (embedded JVM, no Gradle needed)
                       │  [ClassNode] in-process / JSON
                       ▼
    pyjnius-wrap            (Swift 6 + PySwiftAST)
                       │  .py
                       ▼
   pyjnius-style wrapper modules
```

### Extraction Backends

`pyjnius-wrap` supports two extraction backends:

1. **`--backend java`** (default) — Launches `java -jar java-ast-emitter.jar` as a
   subprocess. Requires a JDK on PATH and the bundled JAR. Supports both source
   (JavaParser) and bytecode (ASM) extraction.

2. **`--backend swift-java`** — Uses [swift-java](https://github.com/swiftlang/swift-java)
   to embed a JVM directly in the Swift process and reflect on classes via
   `java.lang.reflect`. No Gradle build, no subprocess, no JSON
   serialization/deserialization. Requires JDK 17+ on PATH (runtime only) and
   Swift 6.2+. Currently supports bytecode/JAR/AAR reflection only (no source
   parsing yet — Phase 4 will add JavaParser-from-Swift for that).

* Stage 1 — `java-ast-emitter/` (Gradle, Kotlin DSL) accepts **either**:
  * a folder of `.java` files (walked via **JavaParser + JavaSymbolSolver**), or
  * a `.jar` / `.aar` / `.class` file or directory of compiled artifacts
    (walked via **ASM 9.7**). This is what lets you wrap closed-source
    SDKs like AdMob, Google Play Services, or `android.jar` directly
    from their Gradle/Maven distribution.

  The backend is auto-detected from the input; pass `--bytecode` to force.
  Both backends emit the same Jackson DTO tree as a single JSON document
  on stdout.
* Stage 2 — `PyjniusWrap/` (SwiftPM) decodes that JSON with `Codable`,
  builds a [PySwiftAST](https://github.com/Py-Swift/PySwiftAST) `Module`
  per class, and renders it via `PySwiftCodeGen.generatePythonCode`.
* The JAR is bundled inside the Swift executable's resources, so the
  end-user only needs `java` on PATH.

## Layout

```
pyjnius-wrapper/
├── java-ast-emitter/                    # Gradle project (Stage 1 — legacy backend)
│   ├── build.gradle.kts
│   ├── src/main/java/dev/kivyschool/pyjniuswrap/
│   │   ├── AstDtos.java                 # Jackson DTOs
│   │   ├── JniDescriptor.java           # JNI signature builder
│   │   ├── ClassExtractor.java          # CompilationUnit walker
│   │   └── JavaAstEmitter.java          # picocli CLI entry
│   └── src/test/java/.../PersonFixtureTest.java
├── PyjniusWrap/                         # SwiftPM package (Stage 2)
│   ├── Package.swift
│   ├── Sources/
│   │   ├── PyjniusWrap/                 # executable target
│   │   │   ├── PyjniusWrap.swift        # ArgumentParser CLI
│   │   │   └── Resources/java-ast-emitter.jar
│   │   ├── PyjniusWrapCore/             # library target
│   │   │   ├── Schema.swift             # Codable mirror of AstDtos.java
│   │   │   ├── PyWrapperEmitter.swift   # ClassNode → PySwiftAST Module
│   │   │   └── Pipeline.swift           # subprocess + file writer
│   │   └── SwiftJavaReflector/          # swift-java backend (Phase 1)
│   │       ├── Reflector.swift          # Embedded JVM reflection
│   │       └── JNIDescriptor.swift      # Type → JNI descriptor conversion
│   └── Tests/
│       ├── PyjniusWrapCoreTests/
│       └── SwiftJavaReflectorTests/
└── fixtures/
    ├── java/com/example/fixture/Person.java
    └── expected/person.ast.json         # golden JSON
```

## Build & test

```sh
# Stage 1: Java (legacy backend only)
cd java-ast-emitter
gradle test shadowJar
# → build/libs/java-ast-emitter.jar

# Stage 2: Swift
cd ../PyjniusWrap
swift test                                # unit tests
swift build -c release                    # → .build/release/pyjnius-wrap
```

The Swift build copies the JAR from `Sources/PyjniusWrap/Resources/`. To
refresh after editing the Java side, rebuild the JAR and copy it back:

```sh
cp java-ast-emitter/build/libs/java-ast-emitter.jar \
   PyjniusWrap/Sources/PyjniusWrap/Resources/
```

### swift-java backend requirements

The `--backend swift-java` path requires:
- **Swift 6.2+** (for swift-java macro support)
- **JDK 17+** on `PATH` or `JAVA_HOME` (runtime only — the JVM is embedded in-process)
- No Gradle, no separate Java build step

## Usage

```sh
# Source folder (JavaParser backend, legacy)
swift run pyjnius-wrap path/to/java/src ./out

# Compiled JAR straight from Maven/Gradle (ASM bytecode backend, auto-detected)
swift run pyjnius-wrap gson-2.11.0.jar ./out

# Single .class, .aar, or directory of compiled artifacts
swift run pyjnius-wrap build/classes ./out

# NEW: swift-java embedded JVM backend (no subprocess, no Gradle needed)
swift run pyjnius-wrap --backend swift-java gson-2.11.0.jar ./out
```

Example — wrap Gson 2.11.0 directly from Maven Central:

```sh
curl -sLo /tmp/gson.jar \
  https://repo1.maven.org/maven2/com/google/code/gson/gson/2.11.0/gson-2.11.0.jar
swift run pyjnius-wrap /tmp/gson.jar /tmp/gson-py
# → 85 .py files under /tmp/gson-py/com/google/gson/...
```

Options:

* `--backend java|swift-java` — extraction backend (default: `java`).
* `--jar PATH`  — override the bundled JAR (use the Gradle output during dev).
* `--java-executable NAME` — override the `java` binary on PATH.
* `--single-file` — emit one `wrappers.py` instead of a package tree.
* `--keep-package-prefix` — preserve full Java package path in output layout.
* `--external-module` — map a Java package to an existing Python module.

## What gets generated

Given `Person.java` with overloaded `greet`, varargs `addTags`, a static
factory, public/protected fields, and two ctors, the generator emits:

```python
from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Person"]

class Person(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/example/fixture/Person"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False)]
    SPECIES = JavaStaticField("Ljava/lang/String;")
    name = JavaField("Ljava/lang/String;")
    age = JavaField("I")
    greet = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    anonymous = JavaStaticMethod("()Lcom/example/fixture/Person;")
    getAge = JavaMethod("()I")
    addTags = JavaMethod("([Ljava/lang/String;)V", varargs=True)
```

## Current limitations / next steps

* **Nested classes** — supported. See `Content` / `Content.Builder` fixture.
  Nested types render as nested Python `class` blocks inside the outer
  `ClassDef`, each carrying its own `__javaclass__` slash form.
* **Interfaces** — supported. `Listener` fixture verifies `JavaInterface`
  base + `MetaJavaClass`, no `__javaconstructor__`, implicit-public
  abstract methods, and implicit static fields (`TAG`).
* **Enums** — supported. `Color` fixture emits each constant as
  `JavaStaticField("L<enum-fqcn>;")`; instance methods like `describe()`
  surface as `JavaMethod`. A richer Python-Enum shadow could be a future
  pass.
* **Generic erasure** — type variables collapse to `Ljava/lang/Object;`.
  This matches pyjnius runtime behaviour but may surprise users.
* **No formatter pass** — output is one statement per line. Pipe through
  `black` / `ruff format` if you want PEP-8 line widths.
* **Symbol resolution gaps (source backend only)** — types from jars not
  on the JavaParser classpath fall back to a heuristic (same-package or
  `java.lang.<Name>` for the well-known names). Provide source for any
  dependency you want resolved precisely, **or** switch to the bytecode
  backend, which always has fully-resolved descriptors.
* **Javadoc / parameter names with bytecode** — javadoc is not present
  in `.class` files at all. Parameter names are preserved only if the
  artifact was compiled with `javac -parameters` (most modern Gradle
  libraries are); otherwise they default to `arg0`, `arg1`, …
* **`--maven <coords>` direct fetch** — not yet implemented. Today you
  download the artifact yourself with `curl` / Gradle / `mvn dependency:get`
  and point `pyjnius-wrap` at the resulting `.jar`.
