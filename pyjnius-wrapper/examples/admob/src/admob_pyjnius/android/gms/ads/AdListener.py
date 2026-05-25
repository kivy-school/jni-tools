from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdListener"]

class AdListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdListener"
    __javaconstructor__ = [("()V", False)]
    onAdClosed = JavaMethod("()V")
    onAdFailedToLoad = JavaMethod("(Lcom/google/android/gms/ads/LoadAdError;)V")
    onAdOpened = JavaMethod("()V")
    onAdLoaded = JavaMethod("()V")
    onAdClicked = JavaMethod("()V")
    onAdImpression = JavaMethod("()V")
    onAdSwipeGestureClicked = JavaMethod("()V")