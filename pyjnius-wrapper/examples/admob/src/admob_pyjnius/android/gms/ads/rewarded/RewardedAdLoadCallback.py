from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RewardedAdLoadCallback"]

class RewardedAdLoadCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/rewarded/RewardedAdLoadCallback"
    __javaconstructor__ = [("()V", False)]