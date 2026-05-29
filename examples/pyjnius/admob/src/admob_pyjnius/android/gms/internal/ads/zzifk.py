from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzifk"]

class zzifk(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzifk"
    zza = JavaMethod("()Ljava/util/List;")
    zzb = JavaMethod("()V")
    zzc = JavaMethod("()Ljava/lang/Object;")