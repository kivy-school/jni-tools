from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgtv"]

class zzgtv(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgtv"
    zza = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzgts;")
    zzb = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzgts;Lcom/google/android/gms/internal/ads/zzgts;)Lcom/google/android/gms/internal/ads/zzgts;")