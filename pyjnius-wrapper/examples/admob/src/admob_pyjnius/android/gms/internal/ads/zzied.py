from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzied"]

class zzied(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzied"
    zza = JavaMethod("()I")
    zzb = JavaMethod("()Lcom/google/android/gms/internal/ads/zzihq;")
    zzc = JavaMethod("()Lcom/google/android/gms/internal/ads/zzihr;")
    zzd = JavaMethod("()Z")
    zze = JavaMethod("()Z")