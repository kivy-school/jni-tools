from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdError"]

class AdError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdError"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/String;Lcom/google/android/gms/ads/AdError;)V", False)]
    UNDEFINED_DOMAIN = JavaStaticField("Ljava/lang/String;")
    getCode = JavaMethod("()I")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getDomain = JavaMethod("()Ljava/lang/String;")
    getCause = JavaMethod("()Lcom/google/android/gms/ads/AdError;")
    toString = JavaMethod("()Ljava/lang/String;")
    zza = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zze;")
    zzb = JavaMethod("()Lorg/json/JSONObject;")