from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbss"]

class zzbss(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbss"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;)V", False), ("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/internal/client/zzbu;)V", False), ("(Landroid/content/Context;Lcom/google/android/gms/ads/internal/client/zzbu;)V", False)]
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    zza = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzeh;Lcom/google/android/gms/ads/AdLoadCallback;)V")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    show = JavaMethod("(Landroid/app/Activity;)V")
    setImmersiveMode = JavaMethod("(Z)V")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    getAppEventListener = JavaMethod("()Lcom/google/android/gms/ads/admanager/AppEventListener;")
    setAppEventListener = JavaMethod("(Lcom/google/android/gms/ads/admanager/AppEventListener;)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")