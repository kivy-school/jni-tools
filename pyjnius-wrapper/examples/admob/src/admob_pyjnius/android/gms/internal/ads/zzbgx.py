from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbgx"]

class zzbgx(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbgx"
    zzc = JavaMethod("()V")
    zzd = JavaMethod("()V")
    zze = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("()V")