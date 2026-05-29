from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbf"]

class zzbf(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzbf"
    zzb = JavaMethod("()V")
    zzc = JavaMethod("(I)V")
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("()V")
    zzh = JavaMethod("()V")
    zzj = JavaMethod("()V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zzi = JavaMethod("()V")