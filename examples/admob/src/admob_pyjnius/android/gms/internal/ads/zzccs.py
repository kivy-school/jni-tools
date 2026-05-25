from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccs"]

class zzccs(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccs"
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("(Lcom/google/android/gms/internal/ads/zzccm;)V")
    zzh = JavaMethod("(I)V")
    zzi = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zzj = JavaMethod("()V")
    zzk = JavaMethod("()V")