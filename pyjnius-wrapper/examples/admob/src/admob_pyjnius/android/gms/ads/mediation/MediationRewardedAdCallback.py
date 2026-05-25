from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationRewardedAdCallback"]

class MediationRewardedAdCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationRewardedAdCallback"
    onUserEarnedReward = JavaMultipleMethod([("(Lcom/google/android/gms/ads/rewarded/RewardItem;)V", False, False), ("()V", False, False)])
    onVideoStart = JavaMethod("()V")
    onVideoComplete = JavaMethod("()V")
    onAdFailedToShow = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")