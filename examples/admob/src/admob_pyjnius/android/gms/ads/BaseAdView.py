from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseAdView"]

class BaseAdView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/BaseAdView"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;Z)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;IIZ)V", False)]
    zza = JavaField("Lcom/google/android/gms/ads/internal/client/zzek;")
    destroy = JavaMethod("()V")
    getAdListener = JavaMethod("()Lcom/google/android/gms/ads/AdListener;")
    getAdSize = JavaMethod("()Lcom/google/android/gms/ads/AdSize;")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    loadAd = JavaMethod("(Lcom/google/android/gms/ads/AdRequest;)V")
    pause = JavaMethod("()V")
    resume = JavaMethod("()V")
    isCollapsible = JavaMethod("()Z")
    isLoading = JavaMethod("()Z")
    setAdListener = JavaMethod("(Lcom/google/android/gms/ads/AdListener;)V")
    setAdSize = JavaMethod("(Lcom/google/android/gms/ads/AdSize;)V")
    setAdUnitId = JavaMethod("(Ljava/lang/String;)V")
    onLayout = JavaMethod("(ZIIII)V")
    onMeasure = JavaMethod("(II)V")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")