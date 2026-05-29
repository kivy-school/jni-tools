from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zziel"]

class zziel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zziel"
    __javaconstructor__ = [("()V", False)]
    zza = JavaField("Lcom/google/android/gms/internal/ads/zziee;")