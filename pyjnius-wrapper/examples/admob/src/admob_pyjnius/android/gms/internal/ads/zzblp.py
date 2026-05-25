from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzblp"]

class zzblp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzblp"
    zzc = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzbln;)V")