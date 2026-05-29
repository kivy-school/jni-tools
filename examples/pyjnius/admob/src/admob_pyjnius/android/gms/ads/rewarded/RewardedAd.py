from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RewardedAd"]

class RewardedAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/rewarded/RewardedAd"
    __javaconstructor__ = [("()V", False)]
    load = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/AdRequest;Lcom/google/android/gms/ads/rewarded/RewardedAdLoadCallback;)V", True, False), ("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/admanager/AdManagerAdRequest;Lcom/google/android/gms/ads/rewarded/RewardedAdLoadCallback;)V", True, False)])
    isAdAvailable = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Z")
    pollAd = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Lcom/google/android/gms/ads/rewarded/RewardedAd;")
    setServerSideVerificationOptions = JavaMethod("(Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions;)V")
    setOnAdMetadataChangedListener = JavaMethod("(Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;)V")
    getOnAdMetadataChangedListener = JavaMethod("()Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;")
    getAdMetadata = JavaMethod("()Landroid/os/Bundle;")
    show = JavaMethod("(Landroid/app/Activity;Lcom/google/android/gms/ads/OnUserEarnedRewardListener;)V")
    getRewardItem = JavaMethod("()Lcom/google/android/gms/ads/rewarded/RewardItem;")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    setImmersiveMode = JavaMethod("(Z)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")