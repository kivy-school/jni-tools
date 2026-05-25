from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzn"]

class zzn(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzn"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzm;")
    zzb = JavaMethod("(Landroid/os/Bundle;)Lcom/google/android/gms/ads/internal/client/zzn;")
    zzc = JavaMethod("(Ljava/util/List;)Lcom/google/android/gms/ads/internal/client/zzn;")
    zzd = JavaMethod("(Z)Lcom/google/android/gms/ads/internal/client/zzn;")
    zze = JavaMethod("(I)Lcom/google/android/gms/ads/internal/client/zzn;")
    zzf = JavaMethod("(I)Lcom/google/android/gms/ads/internal/client/zzn;")
    zzg = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/internal/client/zzn;")
    zzh = JavaMethod("(I)Lcom/google/android/gms/ads/internal/client/zzn;")
    zzi = JavaMethod("(J)Lcom/google/android/gms/ads/internal/client/zzn;")