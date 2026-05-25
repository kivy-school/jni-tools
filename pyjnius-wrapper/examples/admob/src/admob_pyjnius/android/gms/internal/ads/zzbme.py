from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbme"]

class zzbme(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbme"
    zzb = JavaMethod("()Ljava/lang/String;")
    zzc = JavaMethod("()Ljava/util/List;")