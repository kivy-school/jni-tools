from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbrh"]

class zzbrh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbrh"
    __javaconstructor__ = [("()V", False)]
    zze = JavaMethod("(Ljava/lang/String;)V")
    zzf = JavaMethod("()V")