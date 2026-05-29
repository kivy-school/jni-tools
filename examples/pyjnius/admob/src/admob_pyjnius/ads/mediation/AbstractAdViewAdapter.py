from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractAdViewAdapter"]

class AbstractAdViewAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/ads/mediation/AbstractAdViewAdapter"
    __javaconstructor__ = [("()V", False)]
    AD_UNIT_ID_PARAMETER = JavaStaticField("Ljava/lang/String;")
    mAdView = JavaField("Lcom/google/android/gms/ads/AdView;")
    mInterstitialAd = JavaField("Lcom/google/android/gms/ads/interstitial/InterstitialAd;")
    buildExtrasBundle = JavaMethod("(Landroid/os/Bundle;Landroid/os/Bundle;)Landroid/os/Bundle;")
    onDestroy = JavaMethod("()V")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")
    getAdUnitId = JavaMethod("(Landroid/os/Bundle;)Ljava/lang/String;")
    requestBannerAd = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/mediation/MediationBannerListener;Landroid/os/Bundle;Lcom/google/android/gms/ads/AdSize;Lcom/google/android/gms/ads/mediation/MediationAdRequest;Landroid/os/Bundle;)V")
    getBannerView = JavaMethod("()Landroid/view/View;")
    requestInterstitialAd = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/mediation/MediationInterstitialListener;Landroid/os/Bundle;Lcom/google/android/gms/ads/mediation/MediationAdRequest;Landroid/os/Bundle;)V")
    onImmersiveModeUpdated = JavaMethod("(Z)V")
    showInterstitial = JavaMethod("()V")
    requestNativeAd = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/mediation/MediationNativeListener;Landroid/os/Bundle;Lcom/google/android/gms/ads/mediation/NativeMediationAdRequest;Landroid/os/Bundle;)V")
    getVideoController = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")