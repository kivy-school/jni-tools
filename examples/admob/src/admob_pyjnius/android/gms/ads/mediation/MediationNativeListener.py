from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationNativeListener"]

class MediationNativeListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationNativeListener"
    onAdLoaded = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/ads/mediation/UnifiedNativeAdMapper;)V")
    onAdFailedToLoad = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;I)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/ads/AdError;)V", False, False)])
    onAdOpened = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    onAdClosed = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    onAdLeftApplication = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    onAdClicked = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    onAdImpression = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    onVideoEnd = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    zzc = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/internal/ads/zzbnd;)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/internal/ads/zzbnd;Ljava/lang/String;)V")