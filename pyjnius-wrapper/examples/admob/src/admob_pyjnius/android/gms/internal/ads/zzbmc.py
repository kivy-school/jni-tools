from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmc"]

class zzbmc(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmc"
    zzb = JavaMethod("()Ljava/lang/String;")
    zzc = JavaMethod("()Ljava/util/List;")