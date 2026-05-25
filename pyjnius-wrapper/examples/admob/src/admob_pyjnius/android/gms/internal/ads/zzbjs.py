from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbjs"]

class zzbjs(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbjs"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbjp;)V")