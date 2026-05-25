from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationAdCallback"]

class MediationAdCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationAdCallback"
    reportAdClicked = JavaMethod("()V")
    reportAdImpression = JavaMethod("()V")
    onAdOpened = JavaMethod("()V")
    onAdClosed = JavaMethod("()V")