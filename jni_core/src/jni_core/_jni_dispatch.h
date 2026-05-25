/* jni_core dispatch shim.
 *
 * JNI's JNIEnv / JavaVM are pointers to vtables (JNINativeInterface_ /
 * JNIInvokeInterface_). Calling them from Cython directly requires
 * declaring those vtables in full — which is brittle across JDK versions
 * and noisy. Instead we expose a handful of trivial `static inline`
 * functions that perform the vtable indirection in C, where it's a
 * one-liner. Cython cimports them from this header.
 *
 * Only the JNI operations needed by jni_core + the code generator are
 * mirrored. Extend as new emitter features land.
 */
#ifndef JNI_CORE_JNI_DISPATCH_H
#define JNI_CORE_JNI_DISPATCH_H

#include <jni.h>

/* ----- Invocation API (JavaVM) ------------------------------------- */

static inline jint jnicore_AttachCurrentThread(JavaVM* vm, JNIEnv** env, void* args) {
    return (*vm)->AttachCurrentThread(vm, (void**)env, args);
}

static inline jint jnicore_DetachCurrentThread(JavaVM* vm) {
    return (*vm)->DetachCurrentThread(vm);
}

static inline jint jnicore_GetEnv(JavaVM* vm, JNIEnv** env, jint version) {
    return (*vm)->GetEnv(vm, (void**)env, version);
}

/* ----- Class lookup & reference management ------------------------- */

static inline jclass jnicore_FindClass(JNIEnv* env, const char* name) {
    return (*env)->FindClass(env, name);
}

static inline jobject jnicore_NewGlobalRef(JNIEnv* env, jobject obj) {
    return (*env)->NewGlobalRef(env, obj);
}

static inline void jnicore_DeleteGlobalRef(JNIEnv* env, jobject obj) {
    (*env)->DeleteGlobalRef(env, obj);
}

static inline void jnicore_DeleteLocalRef(JNIEnv* env, jobject obj) {
    (*env)->DeleteLocalRef(env, obj);
}

/* ----- Method / Field IDs ------------------------------------------ */

static inline jmethodID jnicore_GetMethodID(JNIEnv* env, jclass c, const char* n, const char* s) {
    return (*env)->GetMethodID(env, c, n, s);
}

static inline jmethodID jnicore_GetStaticMethodID(JNIEnv* env, jclass c, const char* n, const char* s) {
    return (*env)->GetStaticMethodID(env, c, n, s);
}

static inline jfieldID jnicore_GetFieldID(JNIEnv* env, jclass c, const char* n, const char* s) {
    return (*env)->GetFieldID(env, c, n, s);
}

static inline jfieldID jnicore_GetStaticFieldID(JNIEnv* env, jclass c, const char* n, const char* s) {
    return (*env)->GetStaticFieldID(env, c, n, s);
}

/* ----- Exception handling ------------------------------------------ */

static inline jboolean jnicore_ExceptionCheck(JNIEnv* env) {
    return (*env)->ExceptionCheck(env);
}

static inline jthrowable jnicore_ExceptionOccurred(JNIEnv* env) {
    return (*env)->ExceptionOccurred(env);
}

static inline void jnicore_ExceptionDescribe(JNIEnv* env) {
    (*env)->ExceptionDescribe(env);
}

static inline void jnicore_ExceptionClear(JNIEnv* env) {
    (*env)->ExceptionClear(env);
}

/* ----- Strings ----------------------------------------------------- */

static inline jstring jnicore_NewStringUTF(JNIEnv* env, const char* utf) {
    return (*env)->NewStringUTF(env, utf);
}

static inline const char* jnicore_GetStringUTFChars(JNIEnv* env, jstring s, jboolean* iscopy) {
    return (*env)->GetStringUTFChars(env, s, iscopy);
}

static inline void jnicore_ReleaseStringUTFChars(JNIEnv* env, jstring s, const char* utf) {
    (*env)->ReleaseStringUTFChars(env, s, utf);
}

static inline jsize jnicore_GetStringUTFLength(JNIEnv* env, jstring s) {
    return (*env)->GetStringUTFLength(env, s);
}

/* ----- Object instantiation ---------------------------------------- */

static inline jobject jnicore_NewObjectA(JNIEnv* env, jclass c, jmethodID m, const jvalue* a) {
    return (*env)->NewObjectA(env, c, m, a);
}

/* ----- Call*Method variants (instance, A-form) --------------------- */

static inline jobject  jnicore_CallObjectMethodA (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallObjectMethodA (env, o, m, a); }
static inline jboolean jnicore_CallBooleanMethodA(JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallBooleanMethodA(env, o, m, a); }
static inline jbyte    jnicore_CallByteMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallByteMethodA   (env, o, m, a); }
static inline jchar    jnicore_CallCharMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallCharMethodA   (env, o, m, a); }
static inline jshort   jnicore_CallShortMethodA  (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallShortMethodA  (env, o, m, a); }
static inline jint     jnicore_CallIntMethodA    (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallIntMethodA    (env, o, m, a); }
static inline jlong    jnicore_CallLongMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallLongMethodA   (env, o, m, a); }
static inline jfloat   jnicore_CallFloatMethodA  (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallFloatMethodA  (env, o, m, a); }
static inline jdouble  jnicore_CallDoubleMethodA (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) { return (*env)->CallDoubleMethodA (env, o, m, a); }
static inline void     jnicore_CallVoidMethodA   (JNIEnv* env, jobject o, jmethodID m, const jvalue* a) {        (*env)->CallVoidMethodA   (env, o, m, a); }

/* ----- CallStatic*Method variants (A-form) ------------------------- */

static inline jobject  jnicore_CallStaticObjectMethodA (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticObjectMethodA (env, c, m, a); }
static inline jboolean jnicore_CallStaticBooleanMethodA(JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticBooleanMethodA(env, c, m, a); }
static inline jbyte    jnicore_CallStaticByteMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticByteMethodA   (env, c, m, a); }
static inline jchar    jnicore_CallStaticCharMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticCharMethodA   (env, c, m, a); }
static inline jshort   jnicore_CallStaticShortMethodA  (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticShortMethodA  (env, c, m, a); }
static inline jint     jnicore_CallStaticIntMethodA    (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticIntMethodA    (env, c, m, a); }
static inline jlong    jnicore_CallStaticLongMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticLongMethodA   (env, c, m, a); }
static inline jfloat   jnicore_CallStaticFloatMethodA  (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticFloatMethodA  (env, c, m, a); }
static inline jdouble  jnicore_CallStaticDoubleMethodA (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) { return (*env)->CallStaticDoubleMethodA (env, c, m, a); }
static inline void     jnicore_CallStaticVoidMethodA   (JNIEnv* env, jclass c, jmethodID m, const jvalue* a) {        (*env)->CallStaticVoidMethodA   (env, c, m, a); }

/* ----- Get/Set instance fields ------------------------------------- */

static inline jobject  jnicore_GetObjectField (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetObjectField (env, o, f); }
static inline jboolean jnicore_GetBooleanField(JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetBooleanField(env, o, f); }
static inline jbyte    jnicore_GetByteField   (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetByteField   (env, o, f); }
static inline jchar    jnicore_GetCharField   (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetCharField   (env, o, f); }
static inline jshort   jnicore_GetShortField  (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetShortField  (env, o, f); }
static inline jint     jnicore_GetIntField    (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetIntField    (env, o, f); }
static inline jlong    jnicore_GetLongField   (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetLongField   (env, o, f); }
static inline jfloat   jnicore_GetFloatField  (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetFloatField  (env, o, f); }
static inline jdouble  jnicore_GetDoubleField (JNIEnv* env, jobject o, jfieldID f) { return (*env)->GetDoubleField (env, o, f); }

static inline void jnicore_SetObjectField (JNIEnv* env, jobject o, jfieldID f, jobject  v) { (*env)->SetObjectField (env, o, f, v); }
static inline void jnicore_SetBooleanField(JNIEnv* env, jobject o, jfieldID f, jboolean v) { (*env)->SetBooleanField(env, o, f, v); }
static inline void jnicore_SetByteField   (JNIEnv* env, jobject o, jfieldID f, jbyte    v) { (*env)->SetByteField   (env, o, f, v); }
static inline void jnicore_SetCharField   (JNIEnv* env, jobject o, jfieldID f, jchar    v) { (*env)->SetCharField   (env, o, f, v); }
static inline void jnicore_SetShortField  (JNIEnv* env, jobject o, jfieldID f, jshort   v) { (*env)->SetShortField  (env, o, f, v); }
static inline void jnicore_SetIntField    (JNIEnv* env, jobject o, jfieldID f, jint     v) { (*env)->SetIntField    (env, o, f, v); }
static inline void jnicore_SetLongField   (JNIEnv* env, jobject o, jfieldID f, jlong    v) { (*env)->SetLongField   (env, o, f, v); }
static inline void jnicore_SetFloatField  (JNIEnv* env, jobject o, jfieldID f, jfloat   v) { (*env)->SetFloatField  (env, o, f, v); }
static inline void jnicore_SetDoubleField (JNIEnv* env, jobject o, jfieldID f, jdouble  v) { (*env)->SetDoubleField (env, o, f, v); }

/* ----- Get/Set static fields --------------------------------------- */

static inline jobject  jnicore_GetStaticObjectField (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticObjectField (env, c, f); }
static inline jboolean jnicore_GetStaticBooleanField(JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticBooleanField(env, c, f); }
static inline jbyte    jnicore_GetStaticByteField   (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticByteField   (env, c, f); }
static inline jchar    jnicore_GetStaticCharField   (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticCharField   (env, c, f); }
static inline jshort   jnicore_GetStaticShortField  (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticShortField  (env, c, f); }
static inline jint     jnicore_GetStaticIntField    (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticIntField    (env, c, f); }
static inline jlong    jnicore_GetStaticLongField   (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticLongField   (env, c, f); }
static inline jfloat   jnicore_GetStaticFloatField  (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticFloatField  (env, c, f); }
static inline jdouble  jnicore_GetStaticDoubleField (JNIEnv* env, jclass c, jfieldID f) { return (*env)->GetStaticDoubleField (env, c, f); }

static inline void jnicore_SetStaticObjectField (JNIEnv* env, jclass c, jfieldID f, jobject  v) { (*env)->SetStaticObjectField (env, c, f, v); }
static inline void jnicore_SetStaticBooleanField(JNIEnv* env, jclass c, jfieldID f, jboolean v) { (*env)->SetStaticBooleanField(env, c, f, v); }
static inline void jnicore_SetStaticByteField   (JNIEnv* env, jclass c, jfieldID f, jbyte    v) { (*env)->SetStaticByteField   (env, c, f, v); }
static inline void jnicore_SetStaticCharField   (JNIEnv* env, jclass c, jfieldID f, jchar    v) { (*env)->SetStaticCharField   (env, c, f, v); }
static inline void jnicore_SetStaticShortField  (JNIEnv* env, jclass c, jfieldID f, jshort   v) { (*env)->SetStaticShortField  (env, c, f, v); }
static inline void jnicore_SetStaticIntField    (JNIEnv* env, jclass c, jfieldID f, jint     v) { (*env)->SetStaticIntField    (env, c, f, v); }
static inline void jnicore_SetStaticLongField   (JNIEnv* env, jclass c, jfieldID f, jlong    v) { (*env)->SetStaticLongField   (env, c, f, v); }
static inline void jnicore_SetStaticFloatField  (JNIEnv* env, jclass c, jfieldID f, jfloat   v) { (*env)->SetStaticFloatField  (env, c, f, v); }
static inline void jnicore_SetStaticDoubleField (JNIEnv* env, jclass c, jfieldID f, jdouble  v) { (*env)->SetStaticDoubleField (env, c, f, v); }

/* ----- Arrays ------------------------------------------------------- */

static inline jsize jnicore_GetArrayLength(JNIEnv* env, jarray a) { return (*env)->GetArrayLength(env, a); }

static inline jobjectArray  jnicore_NewObjectArray (JNIEnv* env, jsize n, jclass c, jobject init) { return (*env)->NewObjectArray (env, n, c, init); }
static inline jbooleanArray jnicore_NewBooleanArray(JNIEnv* env, jsize n) { return (*env)->NewBooleanArray(env, n); }
static inline jbyteArray    jnicore_NewByteArray   (JNIEnv* env, jsize n) { return (*env)->NewByteArray   (env, n); }
static inline jcharArray    jnicore_NewCharArray   (JNIEnv* env, jsize n) { return (*env)->NewCharArray   (env, n); }
static inline jshortArray   jnicore_NewShortArray  (JNIEnv* env, jsize n) { return (*env)->NewShortArray  (env, n); }
static inline jintArray     jnicore_NewIntArray    (JNIEnv* env, jsize n) { return (*env)->NewIntArray    (env, n); }
static inline jlongArray    jnicore_NewLongArray   (JNIEnv* env, jsize n) { return (*env)->NewLongArray   (env, n); }
static inline jfloatArray   jnicore_NewFloatArray  (JNIEnv* env, jsize n) { return (*env)->NewFloatArray  (env, n); }
static inline jdoubleArray  jnicore_NewDoubleArray (JNIEnv* env, jsize n) { return (*env)->NewDoubleArray (env, n); }

static inline jobject jnicore_GetObjectArrayElement(JNIEnv* env, jobjectArray a, jsize i) { return (*env)->GetObjectArrayElement(env, a, i); }
static inline void    jnicore_SetObjectArrayElement(JNIEnv* env, jobjectArray a, jsize i, jobject v) { (*env)->SetObjectArrayElement(env, a, i, v); }

#define JNICORE_PRIM_ARRAY_REGION(T, J) \
    static inline void jnicore_Get##T##ArrayRegion(JNIEnv* env, J##Array a, jsize s, jsize n, J* b) { (*env)->Get##T##ArrayRegion(env, a, s, n, b); } \
    static inline void jnicore_Set##T##ArrayRegion(JNIEnv* env, J##Array a, jsize s, jsize n, const J* b) { (*env)->Set##T##ArrayRegion(env, a, s, n, b); }

JNICORE_PRIM_ARRAY_REGION(Boolean, jboolean)
JNICORE_PRIM_ARRAY_REGION(Byte,    jbyte)
JNICORE_PRIM_ARRAY_REGION(Char,    jchar)
JNICORE_PRIM_ARRAY_REGION(Short,   jshort)
JNICORE_PRIM_ARRAY_REGION(Int,     jint)
JNICORE_PRIM_ARRAY_REGION(Long,    jlong)
JNICORE_PRIM_ARRAY_REGION(Float,   jfloat)
JNICORE_PRIM_ARRAY_REGION(Double,  jdouble)

#undef JNICORE_PRIM_ARRAY_REGION

#endif /* JNI_CORE_JNI_DISPATCH_H */
