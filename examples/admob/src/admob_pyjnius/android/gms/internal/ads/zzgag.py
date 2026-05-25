from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgag"]

class zzgag(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgag"
    __javaconstructor__ = [("()V", False)]
    zza = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzgas;")
    zzb = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzguj;Lcom/google/android/gms/internal/ads/zzguj;Lcom/google/android/gms/internal/ads/zzgai;)Lcom/google/android/gms/internal/ads/zzgas;")
    zzc = JavaStaticMethod("(ILcom/google/android/gms/internal/ads/zzgai;)Lcom/google/android/gms/internal/ads/zzgas;")