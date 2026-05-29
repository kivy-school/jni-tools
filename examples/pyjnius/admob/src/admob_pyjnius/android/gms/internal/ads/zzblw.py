from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzblw"]

class zzblw(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzblw"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Drawable;Landroid/net/Uri;DIILjava/util/Map;)V", False)]
    zzb = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzc = JavaMethod("()Landroid/net/Uri;")
    zzd = JavaMethod("()D")
    zze = JavaMethod("()I")
    zzf = JavaMethod("()I")
    zzg = JavaMethod("()Ljava/util/Map;")