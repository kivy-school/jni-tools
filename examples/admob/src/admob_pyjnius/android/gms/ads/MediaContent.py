from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaContent"]

class MediaContent(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/MediaContent"
    getAspectRatio = JavaMethod("()F")
    getDuration = JavaMethod("()F")
    getCurrentTime = JavaMethod("()F")
    getVideoController = JavaMethod("()Lcom/google/android/gms/ads/VideoController;")
    hasVideoContent = JavaMethod("()Z")
    setMainImage = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    getMainImage = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    zza = JavaMethod("()Z")
    zzb = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnc;")