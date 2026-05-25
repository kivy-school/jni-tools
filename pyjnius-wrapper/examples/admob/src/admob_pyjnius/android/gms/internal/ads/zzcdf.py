from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcdf"]

class zzcdf(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcdf"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbvp;)V", False)]
    onAdOpened = JavaMethod("()V")
    onAdClosed = JavaMethod("()V")
    onUserEarnedReward = JavaMultipleMethod([("(Lcom/google/android/gms/ads/rewarded/RewardItem;)V", False, False), ("()V", False, False)])
    reportAdClicked = JavaMethod("()V")
    reportAdImpression = JavaMethod("()V")
    onAdFailedToShow = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")
    onVideoStart = JavaMethod("()V")
    onVideoComplete = JavaMethod("()V")