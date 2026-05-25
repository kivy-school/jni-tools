from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbks"]

class zzbks(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbks"
    zza = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")
    zzb = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")
    zzc = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")