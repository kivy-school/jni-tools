from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfo"]

class zzfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfo"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/OnPaidEventListener;)V", False)]
    zzf = JavaMethod("()Z")
    zze = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzt;)V")