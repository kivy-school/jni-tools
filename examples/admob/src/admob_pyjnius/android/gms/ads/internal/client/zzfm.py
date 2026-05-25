from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfm"]

class zzfm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfm"
    __javaconstructor__ = [("()V", False)]
    zzb = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzc = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzm;Lcom/google/android/gms/internal/ads/zzccw;)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzm;Lcom/google/android/gms/internal/ads/zzccw;)V")
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzccs;)V")
    zzf = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzdn;)V")
    zzg = JavaMethod("()Landroid/os/Bundle;")
    zzh = JavaMethod("(Lcom/google/android/gms/internal/ads/zzcdd;)V")
    zzi = JavaMethod("()Z")
    zzj = JavaMethod("()Ljava/lang/String;")
    zzk = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Z)V")
    zzl = JavaMethod("()Lcom/google/android/gms/internal/ads/zzccm;")
    zzm = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzdx;")
    zzn = JavaMethod("()Ljava/lang/String;")
    zzo = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzdq;)V")
    zzp = JavaMethod("(Z)V")
    zzq = JavaMethod("()J")
    zzr = JavaMethod("(J)V")
    zzs = JavaMethod("(Lcom/google/android/gms/internal/ads/zzccx;)V")