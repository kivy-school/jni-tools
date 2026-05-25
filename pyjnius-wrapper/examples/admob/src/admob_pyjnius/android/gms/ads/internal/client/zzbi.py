from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbi"]

class zzbi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzbi"
    zzb = JavaMethod("()V")
    zzc = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")