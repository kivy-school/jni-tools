from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgtp"]

class zzgtp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgtp"
    zzc = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzgtp;")
    zzd = JavaStaticMethod("(Ljava/lang/Object;)Lcom/google/android/gms/internal/ads/zzgtp;")
    zza = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzgti;)Lcom/google/android/gms/internal/ads/zzgtp;")