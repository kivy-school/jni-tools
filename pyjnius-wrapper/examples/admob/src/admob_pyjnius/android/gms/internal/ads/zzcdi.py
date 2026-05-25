from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcdi"]

class zzcdi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcdi"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/rewardedinterstitial/RewardedInterstitialAdLoadCallback;Lcom/google/android/gms/internal/ads/zzcdj;)V", False)]
    zze = JavaMethod("()V")
    zzf = JavaMethod("(I)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")