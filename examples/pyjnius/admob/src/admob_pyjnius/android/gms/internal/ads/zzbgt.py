from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbgt"]

class zzbgt(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbgt"
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbgq;)V")
    zzc = JavaMethod("(I)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")