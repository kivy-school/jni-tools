from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwa"]

class zzbwa(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwa"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbvp;)V", False)]
    reportAdClicked = JavaMethod("()V")
    reportAdImpression = JavaMethod("()V")
    onAdOpened = JavaMethod("()V")
    onAdClosed = JavaMethod("()V")
    onAdLeftApplication = JavaMethod("()V")
    onVideoPause = JavaMethod("()V")
    onVideoPlay = JavaMethod("()V")
    onVideoComplete = JavaMethod("()V")
    onAdFailedToShow = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")
    onVideoMute = JavaMethod("()V")
    onVideoUnmute = JavaMethod("()V")