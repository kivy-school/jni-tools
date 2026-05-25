from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationInterstitialListener"]

class MediationInterstitialListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationInterstitialListener"
    onAdLoaded = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V")
    onAdFailedToLoad = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;I)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;Lcom/google/android/gms/ads/AdError;)V", False, False)])
    onAdOpened = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V")
    onAdClosed = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V")
    onAdLeftApplication = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V")
    onAdClicked = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V")