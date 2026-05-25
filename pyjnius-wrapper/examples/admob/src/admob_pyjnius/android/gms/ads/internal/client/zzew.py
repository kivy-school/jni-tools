from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzew"]

class zzew(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzew"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Ljava/lang/String;")