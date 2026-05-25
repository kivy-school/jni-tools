from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationInterstitialAdCallback"]

class MediationInterstitialAdCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationInterstitialAdCallback"
    onAdLeftApplication = JavaMethod("()V")
    onAdFailedToShow = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")