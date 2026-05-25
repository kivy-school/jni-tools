from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomEventListener"]

class CustomEventListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/customevent/CustomEventListener"
    onAdFailedToLoad = JavaMultipleMethod([("(I)V", False, False), ("(Lcom/google/android/gms/ads/AdError;)V", False, False)])
    onAdOpened = JavaMethod("()V")
    onAdClicked = JavaMethod("()V")
    onAdClosed = JavaMethod("()V")
    onAdLeftApplication = JavaMethod("()V")