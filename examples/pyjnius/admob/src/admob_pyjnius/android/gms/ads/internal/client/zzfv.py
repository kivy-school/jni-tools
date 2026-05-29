from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfv"]

class zzfv(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfv"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/VideoController$VideoLifecycleCallbacks;)V", False)]
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("()V")
    zzh = JavaMethod("()V")
    zzi = JavaMethod("(Z)V")