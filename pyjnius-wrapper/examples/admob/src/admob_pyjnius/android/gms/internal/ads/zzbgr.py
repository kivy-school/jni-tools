from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbgr"]

class zzbgr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbgr"
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbgq;)V")
    zzc = JavaMethod("(I)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")