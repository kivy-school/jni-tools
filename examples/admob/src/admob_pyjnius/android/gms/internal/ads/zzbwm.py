from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwm"]

class zzbwm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwm"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbvp;)V", False)]
    zza = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;Ljava/lang/String;Ljava/lang/String;)V")
    onAdClicked = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V", False, False)])
    onAdClosed = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V", False, False)])
    onAdFailedToLoad = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;I)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;Lcom/google/android/gms/ads/AdError;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;I)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;Lcom/google/android/gms/ads/AdError;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;I)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/ads/AdError;)V", False, False)])
    onAdLeftApplication = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V", False, False)])
    onAdOpened = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V", False, False)])
    onAdLoaded = JavaMultipleMethod([("(Lcom/google/android/gms/ads/mediation/MediationBannerAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationInterstitialAdapter;)V", False, False), ("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/ads/mediation/UnifiedNativeAdMapper;)V", False, False)])
    onAdImpression = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    onVideoEnd = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;)V")
    zzb = JavaMethod("()Lcom/google/android/gms/ads/mediation/UnifiedNativeAdMapper;")
    zzc = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/internal/ads/zzbnd;)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/mediation/MediationNativeAdapter;Lcom/google/android/gms/internal/ads/zzbnd;Ljava/lang/String;)V")
    zze = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnd;")