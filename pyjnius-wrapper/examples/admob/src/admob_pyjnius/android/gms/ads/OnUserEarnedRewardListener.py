from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnUserEarnedRewardListener"]

class OnUserEarnedRewardListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/OnUserEarnedRewardListener"
    onUserEarnedReward = JavaMethod("(Lcom/google/android/gms/ads/rewarded/RewardItem;)V")