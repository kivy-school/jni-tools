from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdapterResponseInfo"]

class AdapterResponseInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdapterResponseInfo"
    getAdapterClassName = JavaMethod("()Ljava/lang/String;")
    getLatencyMillis = JavaMethod("()J")
    getAdError = JavaMethod("()Lcom/google/android/gms/ads/AdError;")
    getCredentials = JavaMethod("()Landroid/os/Bundle;")
    getAdSourceName = JavaMethod("()Ljava/lang/String;")
    getAdSourceId = JavaMethod("()Ljava/lang/String;")
    getAdSourceInstanceName = JavaMethod("()Ljava/lang/String;")
    getAdSourceInstanceId = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    zza = JavaStaticMethod("(Lcom/google/android/gms/ads/internal/client/zzv;)Lcom/google/android/gms/ads/AdapterResponseInfo;")
    zzb = JavaMethod("()Lorg/json/JSONObject;")