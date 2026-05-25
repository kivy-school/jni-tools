from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzaw"]

class zzaw(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzaw"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/internal/client/zzk;Lcom/google/android/gms/ads/internal/client/zzi;Lcom/google/android/gms/ads/internal/client/zzfc;Lcom/google/android/gms/internal/ads/zzboe;Lcom/google/android/gms/internal/ads/zzcdb;Lcom/google/android/gms/internal/ads/zzbzf;Lcom/google/android/gms/internal/ads/zzbof;Lcom/google/android/gms/ads/internal/client/zzl;)V", False)]
    zza = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/internal/client/zzr;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/ads/internal/client/zzbu;")
    zzb = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/internal/client/zzr;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/ads/internal/client/zzbu;")
    zzc = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/ads/internal/client/zzbq;")
    zzd = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/ads/internal/client/zzch;")
    zze = JavaMethod("(Landroid/content/Context;Landroid/widget/FrameLayout;Landroid/widget/FrameLayout;)Lcom/google/android/gms/internal/ads/zzbmp;")
    zzf = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/internal/ads/zzccp;")
    zzg = JavaMethod("(Landroid/app/Activity;)Lcom/google/android/gms/internal/ads/zzbzi;")
    zzh = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/ads/internal/client/zzdt;")
    zzi = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/internal/ads/zzcet;")
    zzj = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/internal/ads/zzbzb;")
    zzk = JavaMethod("(Landroid/content/Context;Lcom/google/android/gms/internal/ads/zzbvj;Lcom/google/android/gms/ads/h5/OnH5AdsEventListener;)Lcom/google/android/gms/internal/ads/zzbra;")