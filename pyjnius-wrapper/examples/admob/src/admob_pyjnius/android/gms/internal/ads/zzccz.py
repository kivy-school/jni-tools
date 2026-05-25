from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccz"]

class zzccz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccz"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzccm;)V", False)]
    getType = JavaMethod("()Ljava/lang/String;")
    getAmount = JavaMethod("()I")