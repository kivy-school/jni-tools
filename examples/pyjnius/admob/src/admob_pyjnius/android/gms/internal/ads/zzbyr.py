from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbyr"]

class zzbyr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbyr"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbml;)V", False)]
    getDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    getScale = JavaMethod("()D")
    zza = JavaMethod("()I")
    zzb = JavaMethod("()I")