from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmx"]

class zzbmx(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmx"
    zzb = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzc = JavaMethod("()Ljava/lang/String;")
    zzd = JavaMethod("()Ljava/util/List;")
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbml;")
    zzg = JavaMethod("()Ljava/lang/String;")
    zzh = JavaMethod("()D")
    zzi = JavaMethod("()Ljava/lang/String;")
    zzj = JavaMethod("()Ljava/lang/String;")
    zzk = JavaMethod("()Landroid/os/Bundle;")
    zzl = JavaMethod("()V")
    zzm = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")
    zzn = JavaMethod("(Landroid/os/Bundle;)V")
    zzo = JavaMethod("(Landroid/os/Bundle;)Z")
    zzp = JavaMethod("(Landroid/os/Bundle;)V")
    zzq = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbme;")
    zzr = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzs = JavaMethod("()Ljava/lang/String;")