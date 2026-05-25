from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbgm"]

class zzbgm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbgm"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbgq;Ljava/lang/String;)V", False), ("(Lcom/google/android/gms/internal/ads/zzbgq;)V", False)]
    show = JavaMethod("(Landroid/app/Activity;)V")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    setImmersiveMode = JavaMethod("(Z)V")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")