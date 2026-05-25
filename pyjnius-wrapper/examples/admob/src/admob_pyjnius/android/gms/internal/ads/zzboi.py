from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzboi"]

class zzboi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzboi"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/formats/zze;Lcom/google/android/gms/ads/formats/zzd;)V", False)]
    zza = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnp;")
    zzb = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnm;")