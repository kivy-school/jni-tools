from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzdq"]

class zzdq(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzdq"
    zze = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzt;)V")
    zzf = JavaMethod("()Z")