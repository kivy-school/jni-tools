from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterstitialAdPreloader"]

class InterstitialAdPreloader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/interstitial/InterstitialAdPreloader"
    start = JavaMultipleMethod([("(Ljava/lang/String;Lcom/google/android/gms/ads/preload/PreloadConfiguration;Lcom/google/android/gms/ads/preload/PreloadCallbackV2;)Z", True, False), ("(Ljava/lang/String;Lcom/google/android/gms/ads/preload/PreloadConfiguration;)Z", True, False)])
    isAdAvailable = JavaStaticMethod("(Ljava/lang/String;)Z")
    getNumAdsAvailable = JavaStaticMethod("(Ljava/lang/String;)I")
    destroy = JavaStaticMethod("(Ljava/lang/String;)Z")
    destroyAll = JavaStaticMethod("()V")
    getConfigurations = JavaStaticMethod("()Ljava/util/Map;")
    getConfiguration = JavaStaticMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/preload/PreloadConfiguration;")
    pollAd = JavaStaticMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/interstitial/InterstitialAd;")