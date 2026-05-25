from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzdg"]

class zzdg(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzdg"
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Ljava/lang/String;")