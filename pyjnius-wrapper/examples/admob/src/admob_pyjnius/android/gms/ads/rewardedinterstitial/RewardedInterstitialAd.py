from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RewardedInterstitialAd"]

class RewardedInterstitialAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/rewardedinterstitial/RewardedInterstitialAd"
    __javaconstructor__ = [("()V", False)]
    load = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/AdRequest;Lcom/google/android/gms/ads/rewardedinterstitial/RewardedInterstitialAdLoadCallback;)V", True, False), ("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/admanager/AdManagerAdRequest;Lcom/google/android/gms/ads/rewardedinterstitial/RewardedInterstitialAdLoadCallback;)V", True, False)])
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    setServerSideVerificationOptions = JavaMethod("(Lcom/google/android/gms/ads/rewarded/ServerSideVerificationOptions;)V")
    setOnAdMetadataChangedListener = JavaMethod("(Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;)V")
    getOnAdMetadataChangedListener = JavaMethod("()Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    getAdMetadata = JavaMethod("()Landroid/os/Bundle;")
    getRewardItem = JavaMethod("()Lcom/google/android/gms/ads/rewarded/RewardItem;")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    show = JavaMethod("(Landroid/app/Activity;Lcom/google/android/gms/ads/OnUserEarnedRewardListener;)V")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    setImmersiveMode = JavaMethod("(Z)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")