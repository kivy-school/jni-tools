from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationBannerListener"]

class MediationBannerListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationBannerListener"
    onAdLoaded = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V")
    onAdFailedToLoad = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;I)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;Lcom/google/android/gms/ads/AdError;)V", False, False)])
    onAdOpened = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V")
    onAdClosed = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V")
    onAdLeftApplication = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V")
    onAdClicked = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V")
    zza = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;Ljava/lang/String;Ljava/lang/String;)V")