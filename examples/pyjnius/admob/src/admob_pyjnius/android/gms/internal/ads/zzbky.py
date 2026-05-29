from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbky"]

class zzbky(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbky"
    zza = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")
    zzb = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")
    zzc = JavaStaticField("Lcom/google/android/gms/internal/ads/zzbkh;")