from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationAppOpenAdCallback"]

class MediationAppOpenAdCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationAppOpenAdCallback"
    onAdFailedToShow = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")