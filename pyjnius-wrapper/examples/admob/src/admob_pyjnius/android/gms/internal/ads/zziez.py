from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zziez"]

class zziez(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zziez"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zziex;Lcom/google/android/gms/internal/ads/zziey;)V", False)]
    get = JavaMethod("(I)Ljava/lang/Object;")
    size = JavaMethod("()I")