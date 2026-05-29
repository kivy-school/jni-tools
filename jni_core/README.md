# jni_core

Tiny Cython runtime that the `jni-wrap cython` generator targets.

It contains **only** what generated code needs to call JNI directly:

- `jni.pxd` — `cdef extern from "jni.h"` declarations (JNIEnv, JavaVM, jobject, jmethodID, ...).
- `core.pxd` / `core.pyx` — `get_env()`, `check_jni_exc()`, base `JavaObject` cdef class with global-ref RAII, method/field-ID cache helpers.
- `conversions.pxi` — inline primitive / jstring / primitive-array converters.

The generator emits per-class `.pyx`/`.pxd` modules that `cimport` from here and call `JNIEnv` directly.

## Building

`jni.h` is located via `$JAVA_HOME/include` (and `include/<platform>`).

```bash
export JAVA_HOME=$(/usr/libexec/java_home)   # macOS
pip install -e .
pytest tests/
```
