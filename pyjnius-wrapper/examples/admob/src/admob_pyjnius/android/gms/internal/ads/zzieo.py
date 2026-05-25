from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzieo"]

class zzieo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzieo"
    values = JavaStaticMethod("()[Lcom/google/android/gms/internal/ads/zzieo;")
    zza = JavaStaticField("Lcom/google/android/gms/internal/ads/zzieo;")
    zzb = JavaStaticField("Lcom/google/android/gms/internal/ads/zzieo;")
    zzc = JavaStaticField("Lcom/google/android/gms/internal/ads/zzieo;")
    zzd = JavaStaticField("Lcom/google/android/gms/internal/ads/zzieo;")
    zze = JavaStaticField("Lcom/google/android/gms/internal/ads/zzieo;")
    zzf = JavaStaticField("Lcom/google/android/gms/internal/ads/zzieo;")
    zzg = JavaStaticField("Lcom/google/android/gms/internal/ads/zzieo;")