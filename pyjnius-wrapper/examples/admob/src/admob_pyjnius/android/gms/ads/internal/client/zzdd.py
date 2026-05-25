from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzdd"]

class zzdd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzdd"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/MuteThisAdListener;)V", False)]
    zze = JavaMethod("()V")