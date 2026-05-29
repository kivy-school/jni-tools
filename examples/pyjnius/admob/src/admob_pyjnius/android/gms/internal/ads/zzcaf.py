from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcaf"]

class zzcaf(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcaf"
    __javaconstructor__ = [("(Landroid/content/Context;Lcom/google/android/gms/ads/internal/util/client/VersionInfoParcel;)V", False), ("(Landroid/content/Context;Lcom/google/android/gms/ads/internal/util/client/VersionInfoParcel;Z)V", False)]
    zza = JavaStaticField("Lcom/google/android/gms/internal/ads/zzcah;")
    zza = JavaStaticMethod("(Landroid/content/Context;)Lcom/google/android/gms/internal/ads/zzcah;")
    zzb = JavaStaticMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/internal/util/client/VersionInfoParcel;)Lcom/google/android/gms/internal/ads/zzcah;")
    zzc = JavaStaticMethod("(Landroid/content/Context;)Lcom/google/android/gms/internal/ads/zzcah;")
    zzd = JavaStaticMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/internal/util/client/VersionInfoParcel;)Lcom/google/android/gms/internal/ads/zzcah;")
    zze = JavaStaticMethod("(Ljava/lang/Throwable;)Ljava/lang/String;")
    zzf = JavaStaticMethod("(Ljava/lang/Throwable;)Ljava/lang/String;")
    zzg = JavaMethod("(Ljava/lang/Thread;Ljava/lang/Throwable;)V")
    zzh = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/String;)V")
    zzi = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/String;F)V")