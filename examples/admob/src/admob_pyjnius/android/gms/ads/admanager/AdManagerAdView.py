from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdManagerAdView"]

class AdManagerAdView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/admanager/AdManagerAdView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False)]
    getVideoController = JavaMethod("()Lcom/google/android/gms/ads/VideoController;")
    setVideoOptions = JavaMethod("(Lcom/google/android/gms/ads/VideoOptions;)V")
    getVideoOptions = JavaMethod("()Lcom/google/android/gms/ads/VideoOptions;")
    getAdSizes = JavaMethod("()[Lcom/google/android/gms/ads/AdSize;")
    getAppEventListener = JavaMethod("()Lcom/google/android/gms/ads/admanager/AppEventListener;")
    loadAd = JavaMethod("(Lcom/google/android/gms/ads/admanager/AdManagerAdRequest;)V")
    setManualImpressionsEnabled = JavaMethod("(Z)V")
    recordManualImpression = JavaMethod("()V")
    setAdSizes = JavaMethod("([Lcom/google/android/gms/ads/AdSize;)V", varargs=True)
    setAppEventListener = JavaMethod("(Lcom/google/android/gms/ads/admanager/AppEventListener;)V")
    zza = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzbu;)Z")