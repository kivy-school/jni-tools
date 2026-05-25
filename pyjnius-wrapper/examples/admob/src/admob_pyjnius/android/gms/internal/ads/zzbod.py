from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbod"]

class zzbod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbod"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzboc;)V", False)]
    zzk = JavaMethod("()Ljava/lang/Object;")
    performClick = JavaMethod("(Landroid/os/Bundle;)V")
    recordImpression = JavaMethod("(Landroid/os/Bundle;)Z")
    reportTouchEvent = JavaMethod("(Landroid/os/Bundle;)V")
    zza = JavaMethod("()Ljava/lang/String;")
    zzb = JavaMethod("()Ljava/util/List;")
    zzc = JavaMethod("()Ljava/lang/String;")
    zzd = JavaMethod("()Lcom/google/android/gms/ads/formats/NativeAd$Image;")
    zze = JavaMethod("()Ljava/lang/String;")
    zzg = JavaMethod("()Ljava/lang/Double;")
    zzh = JavaMethod("()Ljava/lang/String;")
    zzi = JavaMethod("()Ljava/lang/String;")
    zzj = JavaMethod("()Lcom/google/android/gms/ads/VideoController;")
    zzf = JavaMethod("()Ljava/lang/String;")