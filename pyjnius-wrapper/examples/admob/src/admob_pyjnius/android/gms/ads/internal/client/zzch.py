from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzch"]

class zzch(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzch"
    zze = JavaMethod("(Ljava/util/List;Lcom/google/android/gms/ads/internal/client/zzcb;)V")
    zzf = JavaMethod("(Ljava/lang/String;)Z")
    zzg = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzccp;")
    zzh = JavaMethod("(Ljava/lang/String;)Z")
    zzi = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzbgq;")
    zzj = JavaMethod("(Ljava/lang/String;)Z")
    zzk = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/internal/client/zzbu;")
    zzl = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbvj;)V")
    zzm = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/internal/client/zzfp;Lcom/google/android/gms/ads/internal/client/zzce;)Z")
    zzn = JavaMethod("(ILjava/lang/String;)Z")
    zzo = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/internal/client/zzbu;")
    zzp = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzbgq;")
    zzq = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzccp;")
    zzr = JavaMethod("(ILjava/lang/String;)Lcom/google/android/gms/ads/internal/client/zzfp;")
    zzs = JavaMethod("(I)Landroid/os/Bundle;")
    zzt = JavaMethod("(ILjava/lang/String;)I")
    zzu = JavaMethod("(ILjava/lang/String;)Z")
    zzv = JavaMethod("(I)V")