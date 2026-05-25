from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreloadCallback"]

class PreloadCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/preload/PreloadCallback"
    onAdsAvailable = JavaMethod("(Lcom/google/android/gms/ads/preload/PreloadConfiguration;)V")
    onAdsExhausted = JavaMethod("(Lcom/google/android/gms/ads/preload/PreloadConfiguration;)V")