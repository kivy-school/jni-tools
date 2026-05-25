from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzeu"]

class zzeu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzeu"
    zza = JavaStaticField("Ljava/util/Set;")
    zza = JavaMethod("(Lcom/google/android/gms/ads/AdFormat;)Lcom/google/android/gms/ads/preload/zzb;")
    zzb = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/client/zzeu;")
    zzc = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/initialization/OnInitializationCompleteListener;)V")
    zzd = JavaMethod("()V")
    zze = JavaMethod("(Landroid/content/Context;Ljava/util/List;Lcom/google/android/gms/ads/preload/PreloadCallback;)Lcom/google/android/gms/common/api/Status;")
    zzf = JavaMethod("(F)V")
    zzg = JavaMethod("()F")
    zzh = JavaMethod("(Z)V")
    zzi = JavaMethod("()Z")
    zzj = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)V")
    zzk = JavaMethod("(Ljava/lang/Class;)V")
    zzl = JavaMethod("()Lcom/google/android/gms/ads/initialization/InitializationStatus;")
    zzm = JavaMethod("(Landroid/content/Context;)V")
    zzn = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/OnAdInspectorClosedListener;)V")
    zzo = JavaMethod("()Ljava/lang/String;")
    zzp = JavaMethod("()Lcom/google/android/gms/ads/RequestConfiguration;")
    zzq = JavaMethod("(Lcom/google/android/gms/ads/RequestConfiguration;)V")
    zzr = JavaMethod("(Z)Z")
    zzs = JavaMethod("(Ljava/lang/String;)V")