from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbsp"]

class zzbsp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbsp"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbsl;)V")
    zzf = JavaMethod("(I)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")