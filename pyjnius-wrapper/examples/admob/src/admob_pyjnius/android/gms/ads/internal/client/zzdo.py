from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzdo"]

class zzdo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzdo"
    zze = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzt;)V")
    zzf = JavaMethod("()Z")