from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzv"]

class zzv(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzv"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("()Lcom/google/android/gms/ads/internal/util/client/zzx;")
    zzb = JavaStaticMethod("(Lorg/json/JSONObject;)Lcom/google/android/gms/ads/internal/util/client/zzv;")