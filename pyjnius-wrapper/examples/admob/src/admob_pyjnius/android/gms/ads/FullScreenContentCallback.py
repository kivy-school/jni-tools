from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FullScreenContentCallback"]

class FullScreenContentCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/FullScreenContentCallback"
    __javaconstructor__ = [("()V", False)]
    ERROR_CODE_INTERNAL_ERROR = JavaStaticField("I")
    ERROR_CODE_AD_REUSED = JavaStaticField("I")
    ERROR_CODE_NOT_READY = JavaStaticField("I")
    ERROR_CODE_APP_NOT_FOREGROUND = JavaStaticField("I")
    ERROR_CODE_MEDIATION_SHOW_ERROR = JavaStaticField("I")
    onAdFailedToShowFullScreenContent = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")
    onAdShowedFullScreenContent = JavaMethod("()V")
    onAdDismissedFullScreenContent = JavaMethod("()V")
    onAdImpression = JavaMethod("()V")
    onAdClicked = JavaMethod("()V")