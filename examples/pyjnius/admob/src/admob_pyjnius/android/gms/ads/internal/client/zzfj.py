from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfj"]

class zzfj(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfj"
    __javaconstructor__ = [("()V", False)]
    zze = JavaMethod("()V")
    zzj = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzf = JavaMethod("(F)V")
    zzg = JavaMethod("(Ljava/lang/String;)V")
    zzh = JavaMethod("(Z)V")
    zzi = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Ljava/lang/String;)V")
    zzk = JavaMethod("()F")
    zzl = JavaMethod("()Z")
    zzm = JavaMethod("()Ljava/lang/String;")
    zzn = JavaMethod("(Ljava/lang/String;)V")
    zzo = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbvj;)V")
    zzp = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbsd;)V")
    zzq = JavaMethod("()Ljava/util/List;")
    zzr = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzfr;)V")
    zzs = JavaMethod("()V")
    zzt = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzdk;)V")
    zzu = JavaMethod("(Z)V")
    zzv = JavaMethod("(Ljava/lang/String;)V")
    zzw = JavaMethod("()V")