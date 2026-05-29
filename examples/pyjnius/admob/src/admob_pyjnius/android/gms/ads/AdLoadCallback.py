from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdLoadCallback"]

class AdLoadCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdLoadCallback"
    __javaconstructor__ = [("()V", False)]
    onAdLoaded = JavaMethod("(Ljava/lang/Object;)V")
    onAdFailedToLoad = JavaMethod("(Lcom/google/android/gms/ads/LoadAdError;)V")