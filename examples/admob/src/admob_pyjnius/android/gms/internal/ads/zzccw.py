from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccw"]

class zzccw(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccw"
    zze = JavaMethod("()V")
    zzf = JavaMethod("(I)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")