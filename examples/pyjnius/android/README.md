# android-pyjnius (temporary)

**Generated package — do not edit by hand.**

Auto-generated pyjnius wrappers for the Android framework (`android.jar`,
API level 35), produced by `jni-wrap`. This package exists as a
stand-in so other `examples/*` packages can resolve `android.*` types
(`Intent`, `Context`, `Bundle`, `Activity`, …) through a real Python
module instead of synthesizing forward-declared stub classes in every
`.pyi`.

Regenerate with:

```sh
swift run --package-path ../../JniWrap jni-wrap \
    --keep-package-prefix \
    ~/.psproject/android-sdk/platforms/android-35/android.jar \
    examples/android/src
```

A proper hand-curated `android-pyjnius` package will replace this at
some point; downstream `pyproject.toml`s already depend on it by name,
so the swap should be transparent.
