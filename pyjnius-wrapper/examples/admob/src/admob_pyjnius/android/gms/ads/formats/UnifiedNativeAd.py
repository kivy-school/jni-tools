from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnifiedNativeAd"]

class UnifiedNativeAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/UnifiedNativeAd"
    __javaconstructor__ = [("()V", False)]
    performClick = JavaMethod("(Landroid/os/Bundle;)V")
    recordImpression = JavaMethod("(Landroid/os/Bundle;)Z")
    reportTouchEvent = JavaMethod("(Landroid/os/Bundle;)V")
    zza = JavaMethod("()Ljava/lang/String;")
    zzb = JavaMethod("()Ljava/util/List;")
    zzc = JavaMethod("()Ljava/lang/String;")
    zzd = JavaMethod("()Lcom/google/android/gms/ads/formats/NativeAd$Image;")
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Ljava/lang/String;")
    zzg = JavaMethod("()Ljava/lang/Double;")
    zzh = JavaMethod("()Ljava/lang/String;")
    zzi = JavaMethod("()Ljava/lang/String;")
    zzj = JavaMethod("()Lcom/google/android/gms/ads/VideoController;")
    zzk = JavaMethod("()Ljava/lang/Object;")