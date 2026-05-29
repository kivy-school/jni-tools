# cython: language_level=3
"""Inline conversion helpers for generated wrappers.

Included via ``include "jni_core/conversions.pxi"`` in generated .pyx
files (or by jni_core itself). Kept as a .pxi instead of a .pxd because
these are short *inline* expressions, not separately compiled symbols —
each generated module benefits from inlining them at the call site.

Generated code is expected to handle box/unbox manually (e.g. an
``Integer`` parameter is passed as a Python int and wrapped via the
generator-emitted ``Integer.valueOf`` path), so the conversions here
are strictly *primitive* + jstring.
"""
from jni_core.jni cimport (
    jboolean, jbyte, jchar, jshort, jint, jlong, jfloat, jdouble,
    JNI_TRUE, JNI_FALSE,
)


cdef inline jboolean py_to_jboolean(object v):
    return JNI_TRUE if v else JNI_FALSE


cdef inline object jboolean_to_py(jboolean v):
    return True if v == JNI_TRUE else False


cdef inline jbyte   py_to_jbyte  (object v): return <jbyte>(<int>v)
cdef inline jchar   py_to_jchar  (object v): return <jchar>(<int>v) if not isinstance(v, str) else <jchar>ord(v)
cdef inline jshort  py_to_jshort (object v): return <jshort>(<int>v)
cdef inline jint    py_to_jint   (object v): return <jint>(<int>v)
cdef inline jlong   py_to_jlong  (object v): return <jlong>(<long long>v)
cdef inline jfloat  py_to_jfloat (object v): return <jfloat>(<double>v)
cdef inline jdouble py_to_jdouble(object v): return <jdouble>(<double>v)
