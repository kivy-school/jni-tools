from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationBannerAdCallback"]

class MediationBannerAdCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationBannerAdCallback"
    onAdLeftApplication = JavaMethod("()V")