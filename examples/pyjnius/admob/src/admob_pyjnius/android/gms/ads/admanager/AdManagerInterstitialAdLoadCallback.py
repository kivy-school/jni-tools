from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdManagerInterstitialAdLoadCallback"]

class AdManagerInterstitialAdLoadCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/admanager/AdManagerInterstitialAdLoadCallback"
    __javaconstructor__ = [("()V", False)]