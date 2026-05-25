from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgti"]

class zzgti(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgti"
    apply = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")