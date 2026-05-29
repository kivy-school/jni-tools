# cython: language_level=3
"""Dispatch wrappers around jni.h's vtable functions.

These are static inline C wrappers from _jni_dispatch.h. Declaring them
here keeps the calling syntax in .pyx files as plain `func(env, …)`
rather than the awkward `(env[0]).func(env, …)` indirection.
"""
from jni_core.jni cimport (
    jobject, jclass, jstring, jthrowable,
    jarray, jobjectArray,
    jbooleanArray, jbyteArray, jcharArray, jshortArray,
    jintArray, jlongArray, jfloatArray, jdoubleArray,
    jmethodID, jfieldID,
    jboolean, jbyte, jchar, jshort, jint, jlong, jfloat, jdouble, jsize,
    jvalue,
    JNIEnv, JavaVM,
)


cdef extern from "_jni_dispatch.h":
    # --- Invocation API.
    jint jnicore_AttachCurrentThread(JavaVM* vm, JNIEnv** env, void* args) nogil
    jint jnicore_DetachCurrentThread(JavaVM* vm) nogil
    jint jnicore_GetEnv(JavaVM* vm, JNIEnv** env, jint version) nogil

    # --- Class lookup & references.
    jclass  jnicore_FindClass(JNIEnv* env, const char* name) nogil
    jobject jnicore_NewGlobalRef(JNIEnv* env, jobject obj) nogil
    void    jnicore_DeleteGlobalRef(JNIEnv* env, jobject obj) nogil
    void    jnicore_DeleteLocalRef(JNIEnv* env, jobject obj) nogil

    # --- Method / Field IDs.
    jmethodID jnicore_GetMethodID(JNIEnv* env, jclass c, const char* n, const char* s) nogil
    jmethodID jnicore_GetStaticMethodID(JNIEnv* env, jclass c, const char* n, const char* s) nogil
    jfieldID  jnicore_GetFieldID(JNIEnv* env, jclass c, const char* n, const char* s) nogil
    jfieldID  jnicore_GetStaticFieldID(JNIEnv* env, jclass c, const char* n, const char* s) nogil

    # --- Exception handling.
    jboolean    jnicore_ExceptionCheck(JNIEnv* env) nogil
    jthrowable  jnicore_ExceptionOccurred(JNIEnv* env) nogil
    void        jnicore_ExceptionDescribe(JNIEnv* env) nogil
    void        jnicore_ExceptionClear(JNIEnv* env) nogil

    # --- Strings.
    jstring     jnicore_NewStringUTF(JNIEnv* env, const char* utf) nogil
    const char* jnicore_GetStringUTFChars(JNIEnv* env, jstring s, jboolean* iscopy) nogil
    void        jnicore_ReleaseStringUTFChars(JNIEnv* env, jstring s, const char* utf) nogil
    jsize       jnicore_GetStringUTFLength(JNIEnv* env, jstring s) nogil

    # --- Object instantiation.
    jobject jnicore_NewObjectA(JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil

    # --- Instance method calls.
    jobject  jnicore_CallObjectMethodA (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jboolean jnicore_CallBooleanMethodA(JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jbyte    jnicore_CallByteMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jchar    jnicore_CallCharMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jshort   jnicore_CallShortMethodA  (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jint     jnicore_CallIntMethodA    (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jlong    jnicore_CallLongMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jfloat   jnicore_CallFloatMethodA  (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    jdouble  jnicore_CallDoubleMethodA (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil
    void     jnicore_CallVoidMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) nogil

    # --- Static method calls.
    jobject  jnicore_CallStaticObjectMethodA (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jboolean jnicore_CallStaticBooleanMethodA(JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jbyte    jnicore_CallStaticByteMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jchar    jnicore_CallStaticCharMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jshort   jnicore_CallStaticShortMethodA  (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jint     jnicore_CallStaticIntMethodA    (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jlong    jnicore_CallStaticLongMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jfloat   jnicore_CallStaticFloatMethodA  (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    jdouble  jnicore_CallStaticDoubleMethodA (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil
    void     jnicore_CallStaticVoidMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) nogil

    # --- Instance field access.
    jobject  jnicore_GetObjectField (JNIEnv* env, jobject o, jfieldID f) nogil
    jboolean jnicore_GetBooleanField(JNIEnv* env, jobject o, jfieldID f) nogil
    jbyte    jnicore_GetByteField   (JNIEnv* env, jobject o, jfieldID f) nogil
    jchar    jnicore_GetCharField   (JNIEnv* env, jobject o, jfieldID f) nogil
    jshort   jnicore_GetShortField  (JNIEnv* env, jobject o, jfieldID f) nogil
    jint     jnicore_GetIntField    (JNIEnv* env, jobject o, jfieldID f) nogil
    jlong    jnicore_GetLongField   (JNIEnv* env, jobject o, jfieldID f) nogil
    jfloat   jnicore_GetFloatField  (JNIEnv* env, jobject o, jfieldID f) nogil
    jdouble  jnicore_GetDoubleField (JNIEnv* env, jobject o, jfieldID f) nogil

    void jnicore_SetObjectField (JNIEnv* env, jobject o, jfieldID f, jobject  v) nogil
    void jnicore_SetBooleanField(JNIEnv* env, jobject o, jfieldID f, jboolean v) nogil
    void jnicore_SetByteField   (JNIEnv* env, jobject o, jfieldID f, jbyte    v) nogil
    void jnicore_SetCharField   (JNIEnv* env, jobject o, jfieldID f, jchar    v) nogil
    void jnicore_SetShortField  (JNIEnv* env, jobject o, jfieldID f, jshort   v) nogil
    void jnicore_SetIntField    (JNIEnv* env, jobject o, jfieldID f, jint     v) nogil
    void jnicore_SetLongField   (JNIEnv* env, jobject o, jfieldID f, jlong    v) nogil
    void jnicore_SetFloatField  (JNIEnv* env, jobject o, jfieldID f, jfloat   v) nogil
    void jnicore_SetDoubleField (JNIEnv* env, jobject o, jfieldID f, jdouble  v) nogil

    # --- Static field access.
    jobject  jnicore_GetStaticObjectField (JNIEnv* env, jclass c, jfieldID f) nogil
    jboolean jnicore_GetStaticBooleanField(JNIEnv* env, jclass c, jfieldID f) nogil
    jbyte    jnicore_GetStaticByteField   (JNIEnv* env, jclass c, jfieldID f) nogil
    jchar    jnicore_GetStaticCharField   (JNIEnv* env, jclass c, jfieldID f) nogil
    jshort   jnicore_GetStaticShortField  (JNIEnv* env, jclass c, jfieldID f) nogil
    jint     jnicore_GetStaticIntField    (JNIEnv* env, jclass c, jfieldID f) nogil
    jlong    jnicore_GetStaticLongField   (JNIEnv* env, jclass c, jfieldID f) nogil
    jfloat   jnicore_GetStaticFloatField  (JNIEnv* env, jclass c, jfieldID f) nogil
    jdouble  jnicore_GetStaticDoubleField (JNIEnv* env, jclass c, jfieldID f) nogil

    void jnicore_SetStaticObjectField (JNIEnv* env, jclass c, jfieldID f, jobject  v) nogil
    void jnicore_SetStaticBooleanField(JNIEnv* env, jclass c, jfieldID f, jboolean v) nogil
    void jnicore_SetStaticByteField   (JNIEnv* env, jclass c, jfieldID f, jbyte    v) nogil
    void jnicore_SetStaticCharField   (JNIEnv* env, jclass c, jfieldID f, jchar    v) nogil
    void jnicore_SetStaticShortField  (JNIEnv* env, jclass c, jfieldID f, jshort   v) nogil
    void jnicore_SetStaticIntField    (JNIEnv* env, jclass c, jfieldID f, jint     v) nogil
    void jnicore_SetStaticLongField   (JNIEnv* env, jclass c, jfieldID f, jlong    v) nogil
    void jnicore_SetStaticFloatField  (JNIEnv* env, jclass c, jfieldID f, jfloat   v) nogil
    void jnicore_SetStaticDoubleField (JNIEnv* env, jclass c, jfieldID f, jdouble  v) nogil

    # --- Arrays.
    jsize jnicore_GetArrayLength(JNIEnv* env, jarray a) nogil

    jobjectArray  jnicore_NewObjectArray (JNIEnv* env, jsize n, jclass c, jobject init) nogil
    jbooleanArray jnicore_NewBooleanArray(JNIEnv* env, jsize n) nogil
    jbyteArray    jnicore_NewByteArray   (JNIEnv* env, jsize n) nogil
    jcharArray    jnicore_NewCharArray   (JNIEnv* env, jsize n) nogil
    jshortArray   jnicore_NewShortArray  (JNIEnv* env, jsize n) nogil
    jintArray     jnicore_NewIntArray    (JNIEnv* env, jsize n) nogil
    jlongArray    jnicore_NewLongArray   (JNIEnv* env, jsize n) nogil
    jfloatArray   jnicore_NewFloatArray  (JNIEnv* env, jsize n) nogil
    jdoubleArray  jnicore_NewDoubleArray (JNIEnv* env, jsize n) nogil

    jobject jnicore_GetObjectArrayElement(JNIEnv* env, jobjectArray a, jsize i) nogil
    void    jnicore_SetObjectArrayElement(JNIEnv* env, jobjectArray a, jsize i, jobject v) nogil

    void jnicore_GetBooleanArrayRegion(JNIEnv* env, jbooleanArray a, jsize s, jsize n, jboolean* b) nogil
    void jnicore_SetBooleanArrayRegion(JNIEnv* env, jbooleanArray a, jsize s, jsize n, const jboolean* b) nogil
    void jnicore_GetByteArrayRegion   (JNIEnv* env, jbyteArray a, jsize s, jsize n, jbyte* b) nogil
    void jnicore_SetByteArrayRegion   (JNIEnv* env, jbyteArray a, jsize s, jsize n, const jbyte* b) nogil
    void jnicore_GetCharArrayRegion   (JNIEnv* env, jcharArray a, jsize s, jsize n, jchar* b) nogil
    void jnicore_SetCharArrayRegion   (JNIEnv* env, jcharArray a, jsize s, jsize n, const jchar* b) nogil
    void jnicore_GetShortArrayRegion  (JNIEnv* env, jshortArray a, jsize s, jsize n, jshort* b) nogil
    void jnicore_SetShortArrayRegion  (JNIEnv* env, jshortArray a, jsize s, jsize n, const jshort* b) nogil
    void jnicore_GetIntArrayRegion    (JNIEnv* env, jintArray a, jsize s, jsize n, jint* b) nogil
    void jnicore_SetIntArrayRegion    (JNIEnv* env, jintArray a, jsize s, jsize n, const jint* b) nogil
    void jnicore_GetLongArrayRegion   (JNIEnv* env, jlongArray a, jsize s, jsize n, jlong* b) nogil
    void jnicore_SetLongArrayRegion   (JNIEnv* env, jlongArray a, jsize s, jsize n, const jlong* b) nogil
    void jnicore_GetFloatArrayRegion  (JNIEnv* env, jfloatArray a, jsize s, jsize n, jfloat* b) nogil
    void jnicore_SetFloatArrayRegion  (JNIEnv* env, jfloatArray a, jsize s, jsize n, const jfloat* b) nogil
    void jnicore_GetDoubleArrayRegion (JNIEnv* env, jdoubleArray a, jsize s, jsize n, jdouble* b) nogil
    void jnicore_SetDoubleArrayRegion (JNIEnv* env, jdoubleArray a, jsize s, jsize n, const jdouble* b) nogil
