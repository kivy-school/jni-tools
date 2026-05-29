from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zziek"]

class zziek(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zziek"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zziep;)V", False)]