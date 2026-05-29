from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzaz"]

class zzaz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzaz"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Lcom/google/android/gms/ads/AdListener;)V")
    onAdClosed = JavaMethod("()V")
    onAdFailedToLoad = JavaMethod("(Lcom/google/android/gms/ads/LoadAdError;)V")
    onAdOpened = JavaMethod("()V")
    onAdLoaded = JavaMethod("()V")
    onAdImpression = JavaMethod("()V")
    onAdClicked = JavaMethod("()V")