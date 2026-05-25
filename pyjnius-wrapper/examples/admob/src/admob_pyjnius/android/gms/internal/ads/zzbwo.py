from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwo"]

class zzbwo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwo"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/mediation/NativeAdMapper;)V", False)]
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Ljava/util/List;")
    zzg = JavaMethod("()Ljava/lang/String;")
    zzh = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbml;")
    zzi = JavaMethod("()Ljava/lang/String;")
    zzj = JavaMethod("()Ljava/lang/String;")
    zzk = JavaMethod("()D")
    zzl = JavaMethod("()Ljava/lang/String;")
    zzm = JavaMethod("()Ljava/lang/String;")
    zzn = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")
    zzo = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbme;")
    zzp = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzq = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzz = JavaMethod("()F")
    zzA = JavaMethod("()F")
    zzB = JavaMethod("()F")
    zzr = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzs = JavaMethod("()Landroid/os/Bundle;")
    zzt = JavaMethod("()Z")
    zzu = JavaMethod("()Z")
    zzv = JavaMethod("()V")
    zzw = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzx = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzy = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzC = JavaMethod("()V")