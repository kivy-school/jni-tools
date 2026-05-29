from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccy"]

class zzccy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccy"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzccp;)V", False), ("(Landroid/content/Context;Ljava/lang/String;)V", False), ("(Landroid/content/Context;Lcom/google/android/gms/internal/ads/zzccp;)V", False)]
    zza = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzeh;Lcom/google/android/gms/ads/rewarded/RewardedAdLoadCallback;)V")
    setServerSideVerificationOptions = JavaMethod("(Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions;)V")
    setOnAdMetadataChangedListener = JavaMethod("(Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;)V")
    getAdMetadata = JavaMethod("()Landroid/os/Bundle;")
    show = JavaMethod("(Landroid/app/Activity;Lcom/google/android/gms/ads/OnUserEarnedRewardListener;)V")
    getRewardItem = JavaMethod("()Lcom/google/android/gms/ads/rewarded/RewardItem;")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnAdMetadataChangedListener = JavaMethod("()Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    setImmersiveMode = JavaMethod("(Z)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")