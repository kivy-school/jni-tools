from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzblm"]

class zzblm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzblm"
    zza = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")
    zzb = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")