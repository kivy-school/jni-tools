from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzed"]

class zzed(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzed"
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("()V")
    zzh = JavaMethod("()V")
    zzi = JavaMethod("(Z)V")