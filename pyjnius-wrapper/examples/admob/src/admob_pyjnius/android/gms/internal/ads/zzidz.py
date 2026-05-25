from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzidz"]

class zzidz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzidz"
    zzb = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzidz;")
    zzc = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzidz;")
    zzd = JavaMethod("(Lcom/google/android/gms/internal/ads/zzifz;I)Lcom/google/android/gms/internal/ads/zzien;")