from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzt"]

class zzt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzt"
    values = JavaStaticMethod("()[Lcom/google/android/gms/ads/internal/util/client/zzt;")
    zza = JavaStaticField("Lcom/google/android/gms/ads/internal/util/client/zzt;")
    zzb = JavaStaticField("Lcom/google/android/gms/ads/internal/util/client/zzt;")
    zzc = JavaStaticField("Lcom/google/android/gms/ads/internal/util/client/zzt;")
    zzd = JavaStaticField("Lcom/google/android/gms/ads/internal/util/client/zzt;")