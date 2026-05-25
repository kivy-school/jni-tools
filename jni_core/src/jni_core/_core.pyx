# cython: language_level=3
"""jni_core runtime — implementation.

Exposes a tiny stable Cython API for generated wrapper modules. Python
callers see ``get_env()``; everything else is cdef-level surface for the
generated ``.pyx`` files.
"""
from cpython.bytes cimport PyBytes_AsString
from cpython.exc   cimport PyErr_SetString
from libc.stdlib   cimport malloc, free
from libc.string   cimport strlen

from jni_core.jni       cimport (
    JNIEnv, JavaVM,
    jboolean, jint, jsize,
    jobject, jclass, jstring, jthrowable,
    jmethodID, jfieldID,
    JNI_OK, JNI_EDETACHED, JNI_VERSION_1_6, JNI_VERSION_1_8,
    JavaVMInitArgs, JavaVMOption,
    JNI_GetCreatedJavaVMs, JNI_CreateJavaVM,
)
from jni_core._dispatch cimport (
    jnicore_AttachCurrentThread,
    jnicore_GetEnv,
    jnicore_FindClass,
    jnicore_NewGlobalRef,
    jnicore_DeleteGlobalRef,
    jnicore_DeleteLocalRef,
    jnicore_GetMethodID,
    jnicore_GetStaticMethodID,
    jnicore_GetFieldID,
    jnicore_GetStaticFieldID,
    jnicore_ExceptionCheck,
    jnicore_ExceptionOccurred,
    jnicore_ExceptionDescribe,
    jnicore_ExceptionClear,
    jnicore_NewStringUTF,
    jnicore_GetStringUTFChars,
    jnicore_ReleaseStringUTFChars,
    jnicore_GetStringUTFLength,
)


# ---------------------------------------------------------------------------
# JVM bootstrap
# ---------------------------------------------------------------------------

cdef JavaVM* _vm = NULL   # cached after first get_env()


cdef JavaVM* _get_or_create_vm() except NULL:
    """Return a JavaVM*, attaching to an existing one (Android/p4a case) or
    creating one with no extra classpath (desktop dev)."""
    global _vm
    if _vm != NULL:
        return _vm

    cdef JavaVM* found = NULL
    cdef jsize n_vms = 0
    cdef jint rc = JNI_GetCreatedJavaVMs(&found, 1, &n_vms)
    # JNI_GetCreatedJavaVMs writes the first VM pointer into *vmBuf.
    # Cython sees the signature as JavaVM** so we pass &found (JavaVM**).
    if rc == JNI_OK and n_vms > 0 and found != NULL:
        _vm = found
        return _vm

    # No existing VM — create a minimal one (no extra options). Generated
    # code that needs a classpath should call into the JVM via
    # URLClassLoader at runtime; we keep the bootstrap free of policy.
    cdef JavaVMInitArgs args
    args.version = JNI_VERSION_1_8
    args.nOptions = 0
    args.options = NULL
    args.ignoreUnrecognized = 0

    cdef JNIEnv* env = NULL
    cdef JavaVM* vm = NULL
    rc = JNI_CreateJavaVM(&vm, <void**>&env, <void*>&args)
    # &vm is JavaVM**; matches the declared signature.
    if rc != JNI_OK or vm == NULL:
        raise RuntimeError(
            "JNI_CreateJavaVM failed (rc=%d). Set JAVA_HOME to a JDK and "
            "ensure libjvm is reachable, or attach an existing JVM first."
            % rc
        )
    _vm = vm
    return _vm


cdef JNIEnv* get_env() except NULL:
    cdef JavaVM* vm = _get_or_create_vm()
    cdef JNIEnv* env = NULL
    cdef jint rc = jnicore_GetEnv(vm, &env, JNI_VERSION_1_6)
    if rc == JNI_OK and env != NULL:
        return env
    if rc == JNI_EDETACHED:
        rc = jnicore_AttachCurrentThread(vm, &env, NULL)
        if rc == JNI_OK and env != NULL:
            return env
    raise RuntimeError("Could not obtain JNIEnv for current thread (rc=%d)." % rc)


cpdef object py_get_env():
    """Python-visible JNIEnv getter. Returns the raw pointer as an int.

    Mostly useful for smoke tests; generated code uses the cdef ``get_env``.
    """
    cdef JNIEnv* env = get_env()
    return <unsigned long long><void*>env


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

cdef int check_jni_exc(JNIEnv* env) except -1:
    if not jnicore_ExceptionCheck(env):
        return 0
    # We could fetch the exception's getMessage/getClass() and surface
    # those — but that itself needs method-ID lookups against a freshly-
    # described/cleared state. Keep v1 simple: describe to stderr, clear,
    # raise a Python-side JavaException.
    jnicore_ExceptionDescribe(env)
    jnicore_ExceptionClear(env)
    from jni_core import JavaException
    raise JavaException("Java exception (see stderr for details)")


# ---------------------------------------------------------------------------
# JavaObject base
# ---------------------------------------------------------------------------

cdef class JavaObject:
    """Base for every generated wrapper. Owns a JNI global reference."""

    def __cinit__(self):
        self._handle = NULL
        self._env = NULL

    def __dealloc__(self):
        if self._handle != NULL and self._env != NULL:
            jnicore_DeleteGlobalRef(self._env, self._handle)
        self._handle = NULL
        self._env = NULL

    cdef void _adopt_local(self, JNIEnv* env, jobject local) except *:
        """Promote a local ref to a global one, owned by this instance.

        The local ref is deleted after promotion.
        """
        if local == NULL:
            raise RuntimeError("Refusing to wrap a NULL jobject.")
        cdef jobject g = jnicore_NewGlobalRef(env, local)
        jnicore_DeleteLocalRef(env, local)
        if g == NULL:
            raise RuntimeError("NewGlobalRef returned NULL.")
        if self._handle != NULL and self._env != NULL:
            jnicore_DeleteGlobalRef(self._env, self._handle)
        self._handle = g
        self._env = env

    cdef void _adopt_global(self, JNIEnv* env, jobject global_ref) except *:
        """Take ownership of an already-global ref (e.g. cached class)."""
        if global_ref == NULL:
            raise RuntimeError("Refusing to wrap a NULL global jobject.")
        if self._handle != NULL and self._env != NULL:
            jnicore_DeleteGlobalRef(self._env, self._handle)
        self._handle = global_ref
        self._env = env

    cpdef bint is_null(self):
        return self._handle == NULL


# ---------------------------------------------------------------------------
# String conversion
# ---------------------------------------------------------------------------

cdef jstring j_str(JNIEnv* env, object value) except? NULL:
    if value is None:
        return NULL
    cdef bytes b = value.encode("utf-8") if isinstance(value, str) else bytes(value)
    cdef const char* raw = PyBytes_AsString(b)
    cdef jstring out = jnicore_NewStringUTF(env, raw)
    if out == NULL:
        check_jni_exc(env)
        raise RuntimeError("NewStringUTF returned NULL.")
    return out


cdef object py_str(JNIEnv* env, jstring value):
    if value == NULL:
        return None
    cdef const char* utf = jnicore_GetStringUTFChars(env, value, NULL)
    if utf == NULL:
        check_jni_exc(env)
        raise RuntimeError("GetStringUTFChars returned NULL.")
    try:
        return (<bytes>utf[:strlen(utf)]).decode("utf-8")
    finally:
        jnicore_ReleaseStringUTFChars(env, value, utf)


# ---------------------------------------------------------------------------
# Class & ID lookup
# ---------------------------------------------------------------------------

cdef jclass find_class(JNIEnv* env, const char* name) except NULL:
    cdef jclass c = jnicore_FindClass(env, name)
    if c == NULL:
        check_jni_exc(env)
        raise RuntimeError("FindClass(%s) returned NULL." % name.decode("ascii", "replace"))
    return c


cdef jclass find_class_global(JNIEnv* env, const char* name) except NULL:
    cdef jclass local = find_class(env, name)
    cdef jclass g = <jclass>jnicore_NewGlobalRef(env, local)
    jnicore_DeleteLocalRef(env, local)
    if g == NULL:
        raise RuntimeError("NewGlobalRef(class %s) returned NULL." % name.decode("ascii", "replace"))
    return g


cdef jmethodID get_method_id(JNIEnv* env, jclass c, const char* n, const char* sig) except NULL:
    cdef jmethodID m = jnicore_GetMethodID(env, c, n, sig)
    if m == NULL:
        check_jni_exc(env)
        raise RuntimeError("GetMethodID(%s%s) failed." % (n.decode("ascii", "replace"), sig.decode("ascii", "replace")))
    return m


cdef jmethodID get_static_method_id(JNIEnv* env, jclass c, const char* n, const char* sig) except NULL:
    cdef jmethodID m = jnicore_GetStaticMethodID(env, c, n, sig)
    if m == NULL:
        check_jni_exc(env)
        raise RuntimeError("GetStaticMethodID(%s%s) failed." % (n.decode("ascii", "replace"), sig.decode("ascii", "replace")))
    return m


cdef jfieldID get_field_id(JNIEnv* env, jclass c, const char* n, const char* sig) except NULL:
    cdef jfieldID f = jnicore_GetFieldID(env, c, n, sig)
    if f == NULL:
        check_jni_exc(env)
        raise RuntimeError("GetFieldID(%s %s) failed." % (n.decode("ascii", "replace"), sig.decode("ascii", "replace")))
    return f


cdef jfieldID get_static_field_id(JNIEnv* env, jclass c, const char* n, const char* sig) except NULL:
    cdef jfieldID f = jnicore_GetStaticFieldID(env, c, n, sig)
    if f == NULL:
        check_jni_exc(env)
        raise RuntimeError("GetStaticFieldID(%s %s) failed." % (n.decode("ascii", "replace"), sig.decode("ascii", "replace")))
    return f
