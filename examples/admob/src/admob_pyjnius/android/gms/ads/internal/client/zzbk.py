from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbk"]

class zzbk(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzbk"
    zzb = JavaMethod("()V")
    zzc = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")