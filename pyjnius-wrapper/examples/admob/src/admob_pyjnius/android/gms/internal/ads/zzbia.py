from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbia"]

class zzbia(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbia"
    zza = JavaMethod("()V")
    zzb = JavaMethod("(I)Lcom/google/android/gms/internal/ads/zzbia;")