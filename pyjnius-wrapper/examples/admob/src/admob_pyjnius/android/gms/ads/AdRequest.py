from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdRequest"]

class AdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdRequest"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/AbstractAdRequestBuilder;)V", False)]
    ERROR_CODE_INTERNAL_ERROR = JavaStaticField("I")
    ERROR_CODE_INVALID_REQUEST = JavaStaticField("I")
    ERROR_CODE_NETWORK_ERROR = JavaStaticField("I")
    ERROR_CODE_NO_FILL = JavaStaticField("I")
    ERROR_CODE_APP_ID_MISSING = JavaStaticField("I")
    ERROR_CODE_REQUEST_ID_MISMATCH = JavaStaticField("I")
    ERROR_CODE_INVALID_AD_STRING = JavaStaticField("I")
    ERROR_CODE_MEDIATION_NO_FILL = JavaStaticField("I")
    MAX_CONTENT_URL_LENGTH = JavaStaticField("I")
    DEVICE_ID_EMULATOR = JavaStaticField("Ljava/lang/String;")
    zza = JavaField("Lcom/google/android/gms/ads/internal/client/zzeh;")
    getContentUrl = JavaMethod("()Ljava/lang/String;")
    getNeighboringContentUrls = JavaMethod("()Ljava/util/List;")
    getKeywords = JavaMethod("()Ljava/util/Set;")
    getNetworkExtrasBundle = JavaMethod("(Ljava/lang/Class;)Landroid/os/Bundle;")
    getCustomEventExtrasBundle = JavaMethod("(Ljava/lang/Class;)Landroid/os/Bundle;")
    isTestDevice = JavaMethod("(Landroid/content/Context;)Z")
    getCustomTargeting = JavaMethod("()Landroid/os/Bundle;")
    getRequestAgent = JavaMethod("()Ljava/lang/String;")
    getAdString = JavaMethod("()Ljava/lang/String;")
    getPlacementId = JavaMethod("()J")
    zza = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzeh;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/AdRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Lcom/google/android/gms/ads/AdRequest;")
        self = JavaMethod("()Lcom/google/android/gms/ads/AdRequest$Builder;")