from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbyq"]

class zzbyq(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbyq"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbnc;)V", False)]
    start = JavaMethod("()Z")
    setView = JavaMethod("(Landroid/view/View;)V")