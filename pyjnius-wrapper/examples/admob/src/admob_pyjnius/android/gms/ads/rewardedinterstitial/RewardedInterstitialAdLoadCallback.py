from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RewardedInterstitialAdLoadCallback"]

class RewardedInterstitialAdLoadCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/rewardedinterstitial/RewardedInterstitialAdLoadCallback"
    __javaconstructor__ = [("()V", False)]