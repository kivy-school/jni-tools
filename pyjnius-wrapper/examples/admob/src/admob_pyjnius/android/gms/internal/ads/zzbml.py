from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbml"]

class zzbml(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbml"
    zzb = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzc = JavaMethod("()Landroid/net/Uri;")
    zzd = JavaMethod("()D")
    zze = JavaMethod("()I")
    zzf = JavaMethod("()I")
    zzg = JavaMethod("()Ljava/util/Map;")