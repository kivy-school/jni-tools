from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbsd"]

class zzbsd(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbsd"
    zzb = JavaMethod("(Ljava/util/List;)V")