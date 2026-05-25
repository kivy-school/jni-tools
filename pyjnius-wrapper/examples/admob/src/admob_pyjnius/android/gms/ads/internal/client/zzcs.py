from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcs"]

class zzcs(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzcs"
    zzb = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zzc = JavaMethod("()V")
    zzd = JavaMethod("()V")
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")