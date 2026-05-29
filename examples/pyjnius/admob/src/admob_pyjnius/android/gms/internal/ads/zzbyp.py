from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbyp"]

class zzbyp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbyp"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbme;)V", False)]
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getImages = JavaMethod("()Ljava/util/List;")