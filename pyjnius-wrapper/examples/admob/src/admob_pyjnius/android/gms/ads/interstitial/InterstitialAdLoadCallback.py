from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterstitialAdLoadCallback"]

class InterstitialAdLoadCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/interstitial/InterstitialAdLoadCallback"
    __javaconstructor__ = [("()V", False)]