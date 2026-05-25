from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterstitialAd"]

class InterstitialAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/interstitial/InterstitialAd"
    __javaconstructor__ = [("()V", False)]
    load = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/AdRequest;Lcom/google/android/gms/ads/interstitial/InterstitialAdLoadCallback;)V")
    isAdAvailable = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Z")
    pollAd = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Lcom/google/android/gms/ads/interstitial/InterstitialAd;")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    show = JavaMethod("(Landroid/app/Activity;)V")
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    setImmersiveMode = JavaMethod("(Z)V")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")