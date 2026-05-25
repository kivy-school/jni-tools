from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbnm"]

class zzbnm(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbnm"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnc;Ljava/lang/String;)V")