# jni-tools test-suite

Desktop end-to-end tests for the `jni-wrap` CLI on **macOS**. For each backend
(pyjnius, jni_core) the test:

1. Downloads `commons-csv-1.11.0.jar` from Maven Central (cached under
   `~/.cache/jni-tools-tests/`).
2. Runs `jni-wrap <backend> <jar> <tmp_pkg_src>` to freshly regenerate
   the Python wrapper package.
3. Writes a minimal `pyproject.toml` / `setup.py`, builds + installs the
   package into the active virtualenv (or compiles in-place for `jni_core`).
4. Starts a JVM with the jar on the classpath and parses a deterministic
   CSV sample using the generated wrappers, asserting an overview
   (header names, row count).

## Run

```bash
cd jni-tools/test-suite
uv sync
export JAVA_HOME=$(/usr/libexec/java_home)
uv run pytest -q
```

The tests skip cleanly on non-macOS hosts. They require Swift 6 + a JDK on the host.
