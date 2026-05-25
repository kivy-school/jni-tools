from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationInterscrollerAd"]

class MediationInterscrollerAd(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationInterscrollerAd"
    shouldDelegateInterscrollerEffect = JavaMethod("()Z")