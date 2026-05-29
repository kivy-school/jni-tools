# jni-wrap

CLI tool that auto-generates [pyjnius](https://github.com/kivy/pyjnius) Python
wrapper modules from Java source files.

## Pipeline

```
    .java sources    ──┐
                       │
    .jar / .aar / .class ──┤  (compiled artifacts, no source needed)
                       │
                       ▼
   swift-java reflector     (embedded JVM reflection, no custom Java code)
       ─── OR ───
   swift-java + JavaParser  (source-level parsing via JavaParser API)
                       │  [ClassNode] in-process
                       ▼
    jni-wrap            (Swift 6 + PySwiftAST)
                       │  .py
                       ▼
   pyjnius-style wrapper modules
```

### Extraction Backends

`jni-wrap` supports two extraction backends — both are pure Swift calling
Java libraries directly through [swift-java](https://github.com/swiftlang/swift-java):

1. **`--backend swift-java`** (default) — Uses swift-java to embed a JVM directly
   in the Swift process and reflect on classes via `java.lang.reflect`. No Gradle
   build, no subprocess, no JSON serialization/deserialization. Requires JDK 17+
   on PATH (runtime only) and Swift 6.2+. Best for bytecode/JAR/AAR inputs.

2. **`--backend source`** — Uses JavaParser (called directly from Swift via
   swift-java) to parse `.java` source files. Calls the JavaParser API
   (`com.github.javaparser.*`) in-process — no custom Java wrapper code needed.
   Provides javadoc extraction, proper parameter names, and full symbol resolution.
   Requires a JavaParser JAR (with dependencies) on the classpath. Best for
   source-level inputs when you want javadoc in the output.

**Architecture**: The entire codebase is Swift. Java libraries (JavaParser for
source parsing, JVM reflection API for bytecode) are called directly through
swift-java's embedded JVM bridge — no custom Java code exists in this project.

## Layout

```
jni-wrapper/
├── JniWrap/                         # SwiftPM package (pure Swift)
│   ├── Package.swift
│   ├── Sources/
│   │   ├── JniWrap/                 # executable target
│   │   │   └── JniWrap.swift        # ArgumentParser CLI
│   │   ├── JniWrapCore/             # library target
│   │   │   ├── Schema.swift             # AST data model
│   │   │   ├── PyWrapperEmitter.swift   # ClassNode → PySwiftAST Module
│   │   │   ├── PyiStubEmitter.swift     # PEP 484 .pyi stub generation
│   │   │   └── Pipeline.swift           # orchestrator + file writer
│   │   └── SwiftJavaReflector/          # swift-java backends
│   │       ├── Reflector.swift          # Embedded JVM reflection (bytecode)
│   │       ├── SourceParser.swift       # JavaParser API caller (source)
│   │       └── JNIDescriptor.swift      # Type → JNI descriptor conversion
│   └── Tests/
│       ├── JniWrapCoreTests/
│       └── SwiftJavaReflectorTests/
└── fixtures/
    ├── java/com/example/fixture/Person.java
    └── expected/person.ast.json         # golden JSON
```

## Build & test

```sh
cd JniWrap
swift test                                # unit tests
swift build -c release                    # → .build/release/jni-wrap
```

### Requirements

- **Swift 6.2+** (for swift-java macro support)
- **JDK 17+** on `PATH` or `JAVA_HOME` (runtime only — the JVM is embedded in-process)
- For `--backend source`: a JavaParser JAR (with symbol solver dependencies) passed via `--java-parser-jar`
- No Gradle, no separate Java build step, no custom Java code

## Subcommands

`jni-wrap` is a multi-target generator with two emission backends:

| Subcommand | Output | Runtime dependency |
|---|---|---|
| `jni-wrap pyjnius` (default) | pyjnius-style `.py` + `.pyi` wrappers | [pyjnius](https://github.com/kivy/pyjnius) |
| `jni-wrap cython` | Cython `.pyx` + `.pxd` + `.pyi` calling JNI directly | [`jni_core`](../jni_core) |

Both subcommands share the same `<input-dir> <output-dir>` positional
arguments and the same extraction backends (`--backend swift-java|source`).
Run any of them with `--help` for the full flag list.

### Cython subcommand

`jni-wrap cython` emits per-class `.pyx` modules that cimport
[`jni_core`](../jni_core) and dispatch JNI calls directly (no Python →
pyjnius → JNI roundtrip). Layout mirrors the pyjnius output:

```
out/
└── com/example/fixture/
    ├── Person.pyx     # Cython implementation, JNI calls via jni_core
    ├── Person.pxd     # cdef class declaration for cross-module cimports
    ├── Person.pyi     # PEP 484 stub (re-uses the same emitter as pyjnius)
    └── __init__.py
```

```sh
# Generate Cython wrappers for a JAR
swift run jni-wrap cython /tmp/gson.jar /tmp/gson-cy

# Then cythonize them against jni_core
pip install -e ../jni_core
cythonize -i /tmp/gson-cy/**/*.pyx
```

Cython-specific options:

* `--jni-core-import MODULE` — Python module to cimport the runtime from
  (default `jni_core`). Override when shipping a vendored copy.
* `--single-file` — flatten all classes into one `wrappers.{pyx,pxd,pyi}`.
* `--keep-package-prefix` — preserve full reverse-DNS package path
  (default: strip the longest common prefix).

**v1 limitations** baked into the Cython emitter:

* Only the **first overload** per Python method name is wired; siblings
  are listed as `# TODO:` comments. (pyjnius routes overloads via
  `JavaMultipleMethod`; the Cython path needs an explicit dispatcher.)
* Java interfaces emit as plain `cdef class` — there is no
  `PythonJavaClass` equivalent yet.
* Opaque `jobject` returns wrap as bare `JavaObject` rather than the
  typed subclass.
* Nested `cdef` classes are hoisted to file scope (Cython forbids
  nested cdef classes).

## Usage

```sh
# Compiled JAR (default swift-java backend — no subprocess, no Gradle)
swift run jni-wrap gson-2.11.0.jar ./out

# Single .class, .aar, or directory of compiled artifacts
swift run jni-wrap build/classes ./out

# Source files with javadoc extraction (source backend via JavaParser)
swift run jni-wrap --backend source --java-parser-jar /path/to/javaparser-fat.jar path/to/java/src ./out
```

Example — wrap Gson 2.11.0 directly from Maven Central:

```sh
curl -sLo /tmp/gson.jar \
  https://repo1.maven.org/maven2/com/google/code/gson/gson/2.11.0/gson-2.11.0.jar
swift run jni-wrap /tmp/gson.jar /tmp/gson-py
# → 85 .py files under /tmp/gson-py/com/google/gson/...
```

Options:

* `--backend swift-java|source` — extraction backend (default: `swift-java`).
* `--java-parser-jar PATH` — path to JavaParser JAR (for `source` backend).
* `--single-file` — emit one `wrappers.py` instead of a package tree.
* `--keep-package-prefix` — preserve full Java package path in output layout.
* `--external-module` — map a Java package to an existing Python module.

## What gets generated

Given `Person.java` with overloaded `greet`, varargs `addTags`, a static
factory, public/protected fields, and two ctors, the generator emits:

```python
from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
* **Interfaces** — supported. `Listener` fixture verifies the interface is
  projected as a `JavaClass` subclass (pyjnius has no `JavaInterface`
  symbol — use `PythonJavaClass` for the reverse direction) with
  `MetaJavaClass`, no `__javaconstructor__`, implicit-public abstract
  methods, and implicit static fields (`TAG`).
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
  and point `jni-wrap` at the resulting `.jar`.
