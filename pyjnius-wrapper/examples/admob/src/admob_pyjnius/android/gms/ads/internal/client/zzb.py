from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzb"]

class zzb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzb"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/internal/client/zza;)V", False)]
    zzb = JavaMethod("()V")