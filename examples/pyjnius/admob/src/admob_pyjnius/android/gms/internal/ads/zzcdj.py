from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcdj"]

class zzcdj(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcdj"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;)V", False)]
    zza = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzeh;Lcom/google/android/gms/ads/rewardedinterstitial/RewardedInterstitialAdLoadCallback;)V")
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    setServerSideVerificationOptions = JavaMethod("(Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions;)V")
    setOnAdMetadataChangedListener = JavaMethod("(Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;)V")
    getOnAdMetadataChangedListener = JavaMethod("()Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;")
    getAdMetadata = JavaMethod("()Landroid/os/Bundle;")
    getRewardItem = JavaMethod("()Lcom/google/android/gms/ads/rewarded/RewardItem;")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    show = JavaMethod("(Landroid/app/Activity;Lcom/google/android/gms/ads/OnUserEarnedRewardListener;)V")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    setImmersiveMode = JavaMethod("(Z)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")