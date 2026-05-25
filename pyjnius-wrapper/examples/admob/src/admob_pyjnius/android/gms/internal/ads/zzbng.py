from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbng"]

class zzbng(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbng"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbmx;)V")