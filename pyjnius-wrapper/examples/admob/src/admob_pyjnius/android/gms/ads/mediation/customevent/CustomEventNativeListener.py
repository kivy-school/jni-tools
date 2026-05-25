from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomEventNativeListener"]

class CustomEventNativeListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/customevent/CustomEventNativeListener"
    onAdLoaded = JavaMethod("(Lcom/google/android/gms/ads/mediation/UnifiedNativeAdMapper;)V")
    onAdImpression = JavaMethod("()V")