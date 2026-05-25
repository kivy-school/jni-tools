from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractAdRequestBuilder"]

class AbstractAdRequestBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AbstractAdRequestBuilder"
    __javaconstructor__ = [("()V", False)]
    zza = JavaField("Lcom/google/android/gms/ads/internal/client/zzeg;")
    self = JavaMethod("()Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    addKeyword = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    addNetworkExtrasBundle = JavaMethod("(Ljava/lang/Class;Landroid/os/Bundle;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    addCustomEventExtrasBundle = JavaMethod("(Ljava/lang/Class;Landroid/os/Bundle;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    addCustomTargeting = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;", False, False), ("(Ljava/lang/String;Ljava/util/List;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;", False, False)])
    setContentUrl = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    setNeighboringContentUrls = JavaMethod("(Ljava/util/List;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    setRequestAgent = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    setAdString = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    setHttpTimeoutMillis = JavaMethod("(I)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    setPlacementId = JavaMethod("(J)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    zza = JavaMethod("(Landroid/os/Bundle;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    zzb = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    zzc = JavaMethod("(Z)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")
    zzd = JavaMethod("(Z)Lcom/google/android/gms/ads/AbstractAdRequestBuilder;")