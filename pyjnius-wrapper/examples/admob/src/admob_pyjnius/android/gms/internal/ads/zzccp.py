from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccp"]

class zzccp(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccp"
    zzc = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzm;Lcom/google/android/gms/internal/ads/zzccw;)V")
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzccs;)V")
    zzi = JavaMethod("()Z")
    zzj = JavaMethod("()Ljava/lang/String;")
    zzb = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzh = JavaMethod("(Lcom/google/android/gms/internal/ads/zzcdd;)V")
    zzf = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzdn;)V")
    zzg = JavaMethod("()Landroid/os/Bundle;")
    zzk = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Z)V")
    zzl = JavaMethod("()Lcom/google/android/gms/internal/ads/zzccm;")
    zzm = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzdx;")
    zzo = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzdq;)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzm;Lcom/google/android/gms/internal/ads/zzccw;)V")
    zzp = JavaMethod("(Z)V")
    zzn = JavaMethod("()Ljava/lang/String;")
    zzq = JavaMethod("()J")
    zzr = JavaMethod("(J)V")
    zzs = JavaMethod("(Lcom/google/android/gms/internal/ads/zzccx;)V")