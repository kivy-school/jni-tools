from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbsr"]

class zzbsr(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbsr"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbsl;)V")
    zzf = JavaMethod("(I)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")