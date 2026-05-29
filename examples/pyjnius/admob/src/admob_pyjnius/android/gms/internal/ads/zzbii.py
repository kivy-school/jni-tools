from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbii"]

class zzbii(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbii"
    zza = JavaStaticMethod("(Landroid/content/Context;)V")
    zzb = JavaStaticMethod("(Landroid/content/Context;)V")
    zzc = JavaStaticMethod("(Landroid/content/Context;)I")
    zzd = JavaStaticMethod("(Landroid/content/Context;)I")
    zze = JavaStaticMethod("(Landroid/content/Context;)V")