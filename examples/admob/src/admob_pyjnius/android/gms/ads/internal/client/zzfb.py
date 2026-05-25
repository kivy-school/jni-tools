from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfb"]

class zzfb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfb"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbmi;Lcom/google/android/gms/internal/ads/zzbnc;)V", False)]
    getAspectRatio = JavaMethod("()F")
    getDuration = JavaMethod("()F")
    getCurrentTime = JavaMethod("()F")
    getVideoController = JavaMethod("()Lcom/google/android/gms/ads/VideoController;")
    hasVideoContent = JavaMethod("()Z")
    zza = JavaMethod("()Z")
    setMainImage = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    getMainImage = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    zzc = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbmi;")
    zzb = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnc;")