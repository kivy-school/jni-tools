from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomEventAdapter"]

class CustomEventAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/customevent/CustomEventAdapter"
    __javaconstructor__ = [("()V", False)]
    onDestroy = JavaMethod("()V")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")
    getBannerView = JavaMethod("()Landroid/view/View;")
    requestBannerAd = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/mediation/MediationBannerListener;Landroid/os/Bundle;Lcom/google/android/gms/ads/AdSize;Lcom/google/android/gms/ads/mediation/MediationAdRequest;Landroid/os/Bundle;)V")
    requestInterstitialAd = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/mediation/MediationInterstitialListener;Landroid/os/Bundle;Lcom/google/android/gms/ads/mediation/MediationAdRequest;Landroid/os/Bundle;)V")
    requestNativeAd = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/mediation/MediationNativeListener;Landroid/os/Bundle;Lcom/google/android/gms/ads/mediation/NativeMediationAdRequest;Landroid/os/Bundle;)V")
    showInterstitial = JavaMethod("()V")