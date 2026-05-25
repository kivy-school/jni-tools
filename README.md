# jni-tools

Tooling and pre-generated packages for calling Java / Android APIs from
Python via [pyjnius](https://github.com/kivy/pyjnius).

This repo contains two complementary halves:

| Path                | What it is |
| ------------------- | ---------- |
| [`pyjnius-wrapper/`](pyjnius-wrapper/) | **The generator.** A Swift 6 CLI (`pyjnius-wrap`) + a JDK 21 Java AST emitter that turn `.java` / `.jar` / `.aar` inputs into pyjnius-style Python wrappers plus PEP 561 `.pyi` stubs. |
| [`examples/`](examples/)               | **Pre-generated, installable Python packages** produced by that generator, ready to drop into a Kivy / Buildozer / pyjnius project. |

## Pre-built packages (`examples/`)

| Package           | Version | Wraps                                       | Notes |
| ----------------- | ------- | ------------------------------------------- | ----- |
| `android-pyjnius`   | 35.0.0  | `android.jar` (Android SDK platform 35)     | Foundation package — every other wrapper imports `android.*` from here. |
| `onesignal-pyjnius` | 4.8.10  | OneSignal Android SDK AAR                   | Routes `android.*` refs to `android-pyjnius` via `--external-module`. |
| `admob-pyjnius`     | 25.3.0  | Google Mobile Ads (AdMob) SDK AAR           | Same — depends on `android-pyjnius`. |

Each is a standard `pyproject.toml` / `hatchling` package. Install
locally with:

```sh
pip install ./examples/android
pip install ./examples/admob       # or ./examples/onesignal
```

Then in Python (inside a running Android/pyjnius context):

```python
from android.view import View
from admob_pyjnius.ads import AdView, AdRequest
```

Type checkers (`pyright`, `mypy`) pick up the bundled `.pyi` stubs
automatically.

## The generator (`pyjnius-wrapper/`)

Generates the packages above — and any other pyjnius wrapper you need —
from compiled JVM artifacts. No Java source required.

```
.java sources        ─┐
.jar / .aar / .class ─┤──►  java-ast-emitter.jar  ──JSON──►  pyjnius-wrap  ──►  .py + .pyi
                      ┘      (JavaParser or ASM)            (Swift 6, SwiftPM)
```

Basic usage:

```sh
cd pyjnius-wrapper/PyjniusWrap
swift build -c release

# Wrap a jar straight from Maven Central (uses swift-java embedded JVM by default):
.build/release/pyjnius-wrap /path/to/some-lib.jar ./out
```

Key flags:

* `--backend swift-java` *(default)* — use the embedded JVM reflector
  for bytecode/JAR/AAR (no Gradle, no subprocess). Requires JDK 17+ on `PATH`.
* `--backend source` — use JavaParser (called in-process via swift-java) for
  `.java` source files. Provides javadoc extraction, parameter names, and full
  symbol resolution. Requires the bundled `java-ast-emitter.jar`.
* `--backend java` *(deprecated)* — use the legacy `java-ast-emitter.jar`
  subprocess. Will be removed in a future release.
* `--keep-package-prefix` — preserve the original Java package
  (`android.view.View` stays at `android/view/View.py` rather than
  having a common prefix stripped). Use this for foundation packages.
* `--external-module <java.prefix.>=<python.prefix>` *(repeatable)* —
  forward type references to an already-published Python package
  instead of synthesizing local stubs. Example:
  `--external-module android.=android` makes generated stubs import
  Android types from `android-pyjnius`.
* `--single-file` — emit one combined module instead of a package tree.

### `.pyi` type resolution

The stub emitter walks a 6-tier priority pipeline for every Java type
reference:

1. Builtin map (`java.lang.String` → `str`, `void` → `None`, …)
2. Same-file nested class (quoted forward reference)
3. Cross-file wrapped import (another file in the same run)
4. `--external-module` mapping (import from an upstream package)
5. Synthesized empty stub — with a docstring carrying the original
   FQCN plus a JavaDoc URL routed by package
   (`android.*` → developer.android.com, `java.*` →
   docs.oracle.com/javase/8, `kotlin.*` → kotlinlang.org,
   `com.google.android.gms.*` / `com.google.firebase.*` →
   developers.google.com/android/reference)
6. `typing.Any` (last resort)

See [`pyjnius-wrapper/wrap-android-module.md`](pyjnius-wrapper/wrap-android-module.md)
for the full recipe and [`pyjnius-wrapper/auto-wrap-java-classes.md`](pyjnius-wrapper/auto-wrap-java-classes.md)
for the single-class / source-folder walkthrough.

## Layout

```
jni-tools/
├── examples/                       # pre-generated, pip-installable packages
│   ├── android/                    #   android-pyjnius 35.0.0
│   ├── admob/                      #   admob-pyjnius 25.3.0
│   └── onesignal/                  #   onesignal-pyjnius 4.8.10
└── pyjnius-wrapper/                # the generator
    ├── PyjniusWrap/                #   Swift 6 SwiftPM package — CLI + codegen
    ├── java-ast-emitter/           #   JDK 21 Gradle — Java→JSON AST emitter
    ├── examples/                   #   in-repo example outputs for the generator
    ├── fixtures/                   #   shared test fixtures
    ├── README.md
    ├── auto-wrap-java-classes.md   #   how-to: single class / source dir
    └── wrap-android-module.md      #   how-to: whole jar/aar + resolution ref
```

## Requirements

* Swift 6.2+ toolchain (Xcode 16+ or swift.org) — swift-java requires 6.2+
* JDK 17+ (`java` on `PATH` at runtime — swift-java embeds the JVM
  in-process; no Gradle/Maven build step needed)
* Python 3.10+ to consume the generated packages (with `pyjnius`
  installed in the Android runtime)

## License

[MIT](LICENSE)
