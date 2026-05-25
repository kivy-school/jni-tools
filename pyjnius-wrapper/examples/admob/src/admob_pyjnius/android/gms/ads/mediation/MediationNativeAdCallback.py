from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationNativeAdCallback"]

class MediationNativeAdCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationNativeAdCallback"
    onAdLeftApplication = JavaMethod("()V")
    onVideoPause = JavaMethod("()V")
    onVideoPlay = JavaMethod("()V")
    onVideoComplete = JavaMethod("()V")
    onVideoMute = JavaMethod("()V")
    onVideoUnmute = JavaMethod("()V")