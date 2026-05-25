from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzff"]

class zzff(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzff"
    __javaconstructor__ = [("()V", False)]
    zzf = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzbh;)V")
    zzj = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbma;)V")
    zzl = JavaMethod("(Lcom/google/android/gms/ads/formats/PublisherAdViewOptions;)V")
    zzp = JavaMethod("(Lcom/google/android/gms/ads/formats/AdManagerAdViewOptions;)V")
    zzn = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbsi;)V")
    zzg = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbng;)V")
    zzm = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnw;)V")
    zzo = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbsr;)V")
    zzh = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnj;)V")
    zzi = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbnp;Lcom/google/android/gms/internal/ads/zzbnm;)V")
    zzk = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnt;Lcom/google/android/gms/ads/internal/client/zzr;)V")
    zze = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzbn;")
    zzb = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzbn;")
    zzq = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzcp;)V")