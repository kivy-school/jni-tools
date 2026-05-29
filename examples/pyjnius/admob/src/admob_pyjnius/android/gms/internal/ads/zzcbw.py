from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcbw"]

class zzcbw(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcbw"
    zzb = JavaMethod("()Ljava/lang/String;")
    zzc = JavaMethod("()I")