from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzx"]

class zzbzx(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzx"
    zze = JavaMethod("(Ljava/util/List;)V")
    zzf = JavaMethod("(Ljava/lang/String;)V")