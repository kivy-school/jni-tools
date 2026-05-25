from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzba"]

class zzba(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzba"
    __javaconstructor__ = [("()V", False)]
    zza = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzbiq;")
    zzb = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzbip;")
    zzc = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzbiv;")
    zzd = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzbig;")