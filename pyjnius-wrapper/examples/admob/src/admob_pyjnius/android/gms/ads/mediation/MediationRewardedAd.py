from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationRewardedAd"]

class MediationRewardedAd(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationRewardedAd"
    showAd = JavaMethod("(Landroid/content/Context;)V")