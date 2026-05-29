# cython: language_level=3
"""Public Cython surface for jni_core.

Generated wrapper modules cimport from here. Everything performance-
critical is a `cdef` / `cpdef` function or a `cdef class` so the call
path stays in C.

The shape is intentionally minimal:

- ``get_env()`` — return a JNIEnv* for the current thread.
- ``check_jni_exc(env)`` — raise ``JavaException`` if a Java exception
  is pending.
- ``JavaObject`` — base cdef class holding a global ref + JNIEnv.
- ``j_str`` / ``py_str`` — string conversion shims.
- ``get_method_id``/``get_field_id`` cache helpers — generated modules
  call these once (lazy at first use) and then store the IDs in
  module-level cdef variables.
"""
from jni_core.jni cimport (
    JNIEnv, jclass, jobject, jstring,
    jmethodID, jfieldID,
)


cdef JNIEnv* get_env() except NULL
cpdef object py_get_env()

cdef int check_jni_exc(JNIEnv* env) except -1

cdef class JavaObject:
    cdef jobject _handle           # global ref; freed in __dealloc__
    cdef JNIEnv* _env              # cached env (per-thread)
    cdef void _adopt_local(self, JNIEnv* env, jobject local) except *
    cdef void _adopt_global(self, JNIEnv* env, jobject global_ref) except *
    cpdef bint is_null(self)


# String shims. Caller passes a Python str; returns a *local* jstring
# ref the caller must release (or hand to the JVM via NewObjectA/Call*).
cdef jstring j_str(JNIEnv* env, object value) except? NULL
cdef object  py_str(JNIEnv* env, jstring value)

# Class & ID lookup helpers. These wrap FindClass / GetMethodID etc. and
# raise JavaException on failure. They do NOT cache — callers cache the
# returned values in module-level cdef variables themselves.
cdef jclass    find_class(JNIEnv* env, const char* name) except NULL
cdef jclass    find_class_global(JNIEnv* env, const char* name) except NULL
cdef jmethodID get_method_id      (JNIEnv* env, jclass c, const char* n, const char* sig) except NULL
cdef jmethodID get_static_method_id(JNIEnv* env, jclass c, const char* n, const char* sig) except NULL
cdef jfieldID  get_field_id       (JNIEnv* env, jclass c, const char* n, const char* sig) except NULL
cdef jfieldID  get_static_field_id(JNIEnv* env, jclass c, const char* n, const char* sig) except NULL
