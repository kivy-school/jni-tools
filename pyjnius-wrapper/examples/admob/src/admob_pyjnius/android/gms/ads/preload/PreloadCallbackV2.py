from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreloadCallbackV2"]

class PreloadCallbackV2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/preload/PreloadCallbackV2"
    __javaconstructor__ = [("()V", False)]
    onAdsExhausted = JavaMethod("(Ljava/lang/String;)V")
    onAdPreloaded = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/ResponseInfo;)V")
    onAdFailedToPreload = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/AdError;)V")