from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzifb"]

class zzifb(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzifb"
    zzb = JavaMethod("()V")
    zza = JavaMethod("()Z")
    zzh = JavaMethod("(I)Lcom/google/android/gms/internal/ads/zzifb;")