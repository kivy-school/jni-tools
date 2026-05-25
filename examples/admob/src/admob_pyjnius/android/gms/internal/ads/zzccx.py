from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccx"]

class zzccx(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccx"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzccm;Ljava/lang/String;Ljava/lang/String;)V")