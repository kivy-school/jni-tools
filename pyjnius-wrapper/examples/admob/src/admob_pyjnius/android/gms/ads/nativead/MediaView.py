from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaView"]

class MediaView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/nativead/MediaView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setMediaContent = JavaMethod("(Lcom/google/android/gms/ads/MediaContent;)V")
    getMediaContent = JavaMethod("()Lcom/google/android/gms/ads/MediaContent;")
    setImageScaleType = JavaMethod("(Landroid/widget/ImageView$ScaleType;)V")
    zza = JavaMethod("(Lcom/google/android/gms/internal/ads/zzblx;)V")
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzblz;)V")