from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResponseInfo"]

class ResponseInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/ResponseInfo"
    getMediationAdapterClassName = JavaMethod("()Ljava/lang/String;")
    getResponseId = JavaMethod("()Ljava/lang/String;")
    getResponseExtras = JavaMethod("()Landroid/os/Bundle;")
    getAdapterResponses = JavaMethod("()Ljava/util/List;")
    getLoadedAdapterResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/AdapterResponseInfo;")
    toString = JavaMethod("()Ljava/lang/String;")
    zza = JavaMethod("()Lorg/json/JSONObject;")
    zzb = JavaStaticMethod("(Lcom/google/android/gms/ads/internal/client/zzdx;)Lcom/google/android/gms/ads/ResponseInfo;")
    zzc = JavaStaticMethod("(Lcom/google/android/gms/ads/internal/client/zzdx;)Lcom/google/android/gms/ads/ResponseInfo;")
    zzd = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzdx;")