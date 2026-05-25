from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbkt"]

class zzbkt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbkt"
    zza = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")
    zzb = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")