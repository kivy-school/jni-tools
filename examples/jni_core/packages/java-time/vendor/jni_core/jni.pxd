# cython: language_level=3
"""Minimal cdef extern declarations for jni.h.

Only the JNI surface our generated wrappers (and runtime helpers) need.
Add more entries as new emitter passes require them; do not vendor the
full jni.h symbol set wholesale — that just creates breakage when JDKs
disagree on opaque struct layouts.
"""

cdef extern from "jni.h":
    # --- Primitive aliases (opaque to Cython; sizes come from jni.h itself).
    ctypedef int             jint
    ctypedef long long       jlong
    ctypedef signed char     jbyte
    ctypedef unsigned short  jchar
    ctypedef short           jshort
    ctypedef float           jfloat
    ctypedef double          jdouble
    ctypedef unsigned char   jboolean
    ctypedef int             jsize

    # --- Opaque reference types.
    ctypedef void* jobject
    ctypedef jobject jclass
    ctypedef jobject jstring
    ctypedef jobject jarray
    ctypedef jarray  jobjectArray
    ctypedef jarray  jbooleanArray
    ctypedef jarray  jbyteArray
    ctypedef jarray  jcharArray
    ctypedef jarray  jshortArray
    ctypedef jarray  jintArray
    ctypedef jarray  jlongArray
    ctypedef jarray  jfloatArray
    ctypedef jarray  jdoubleArray
    ctypedef jobject jthrowable

    # --- Method/Field IDs.
    ctypedef struct _jmethodID
    ctypedef _jmethodID* jmethodID
    ctypedef struct _jfieldID
    ctypedef _jfieldID* jfieldID

    # --- jvalue union (used by Call*MethodA / NewObjectA).
    ctypedef union jvalue:
        jboolean z
        jbyte    b
        jchar    c
        jshort   s
        jint     i
        jlong    j
        jfloat   f
        jdouble  d
        jobject  l

    # --- Boolean constants.
    cdef jboolean JNI_TRUE
    cdef jboolean JNI_FALSE

    # --- VM/Env structs (we use them as opaque pointers and dispatch via
    # explicit function calls below; the actual vtable lives in jni.h
    # behind a function-pointer table that's too noisy to mirror here).
    ctypedef struct JavaVM_
    ctypedef JavaVM_* JavaVM
    ctypedef struct JNIEnv_
    ctypedef JNIEnv_* JNIEnv

    # --- Return codes.
    cdef int JNI_OK
    cdef int JNI_ERR
    cdef int JNI_EDETACHED
    cdef int JNI_EVERSION
    cdef int JNI_VERSION_1_6
    cdef int JNI_VERSION_1_8

    # --- Init args for JNI_CreateJavaVM.
    ctypedef struct JavaVMOption:
        const char* optionString
        void*       extraInfo

    ctypedef struct JavaVMInitArgs:
        jint          version
        jint          nOptions
        JavaVMOption* options
        jboolean      ignoreUnrecognized

    ctypedef struct JavaVMAttachArgs:
        jint        version
        const char* name
        jobject     group

    # --- Invocation API (these *are* plain C functions, not method
    # pointers, so we can declare them directly).
    jint JNI_GetCreatedJavaVMs(JavaVM** vmBuf, jsize bufLen, jsize* nVMs) nogil
    jint JNI_CreateJavaVM(JavaVM** p_vm, void** p_env, void* vm_args) nogil
    jint JNI_GetDefaultJavaVMInitArgs(void* vm_args) nogil
