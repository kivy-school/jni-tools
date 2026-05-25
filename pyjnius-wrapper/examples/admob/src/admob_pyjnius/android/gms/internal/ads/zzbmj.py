from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmj"]

class zzbmj(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmj"
    zzb = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzc = JavaMethod("()Landroid/net/Uri;")
    zzd = JavaMethod("()D")
    zze = JavaMethod("()I")
    zzf = JavaMethod("()I")
    zzg = JavaMethod("()Ljava/util/Map;")