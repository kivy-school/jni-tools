from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdManagerInterstitialAd"]

class AdManagerInterstitialAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/admanager/AdManagerInterstitialAd"
    __javaconstructor__ = [("()V", False)]
    load = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/admanager/AdManagerAdRequest;Lcom/google/android/gms/ads/admanager/AdManagerInterstitialAdLoadCallback;)V")
    getAppEventListener = JavaMethod("()Lcom/google/android/gms/ads/admanager/AppEventListener;")
    setAppEventListener = JavaMethod("(Lcom/google/android/gms/ads/admanager/AppEventListener;)V")