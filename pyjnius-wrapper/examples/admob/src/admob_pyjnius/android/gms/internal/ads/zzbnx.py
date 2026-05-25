from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbnx"]

class zzbnx(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbnx"
    zze = JavaMethod("(Ljava/lang/String;)V")
    zzf = JavaMethod("()V")