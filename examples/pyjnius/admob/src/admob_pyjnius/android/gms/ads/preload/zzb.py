from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzb"]

class zzb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/preload/zzb"
    __javaconstructor__ = [("(Landroid/content/Context;Lcom/google/android/gms/ads/AdFormat;)V", False)]
    zza = JavaField("Lcom/google/android/gms/ads/internal/client/zzch;")
    zzb = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/preload/PreloadConfiguration;Lcom/google/android/gms/ads/preload/PreloadCallbackV2;)Z")
    zzc = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/preload/PreloadConfiguration;)Z")
    zzd = JavaMethod("(Ljava/lang/String;)Z")
    zze = JavaMethod("(Ljava/lang/String;)I")
    zzf = JavaMethod("(Ljava/lang/String;)Z")
    zzg = JavaMethod("()V")
    zzh = JavaMethod("()Ljava/util/Map;")
    zzi = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/preload/PreloadConfiguration;")
    zzj = JavaMethod("()Landroid/content/Context;")