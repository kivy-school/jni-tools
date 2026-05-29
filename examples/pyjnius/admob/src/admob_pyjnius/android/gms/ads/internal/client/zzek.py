from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzek"]

class zzek(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzek"
    __javaconstructor__ = [("(Landroid/view/ViewGroup;I)V", False), ("(Landroid/view/ViewGroup;Landroid/util/AttributeSet;Z)V", False), ("(Landroid/view/ViewGroup;Landroid/util/AttributeSet;ZI)V", False)]
    zza = JavaMethod("()V")
    zzb = JavaMethod("()Lcom/google/android/gms/ads/AdListener;")
    zzc = JavaMethod("()Lcom/google/android/gms/ads/AdSize;")
    zzd = JavaMethod("()[Lcom/google/android/gms/ads/AdSize;")
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Lcom/google/android/gms/ads/admanager/AppEventListener;")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzeh;)V")
    zzh = JavaMethod("()V")
    zzi = JavaMethod("()V")
    zzj = JavaMethod("()V")
    zzk = JavaMethod("(Lcom/google/android/gms/ads/AdListener;)V")
    zzl = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zza;)V")
    zzm = JavaMethod("([Lcom/google/android/gms/ads/AdSize;)V", varargs=True)
    zzn = JavaMethod("([Lcom/google/android/gms/ads/AdSize;)V", varargs=True)
    zzo = JavaMethod("(Ljava/lang/String;)V")
    zzp = JavaMethod("(Lcom/google/android/gms/ads/admanager/AppEventListener;)V")
    zzq = JavaMethod("(Z)V")
    zzr = JavaMethod("()Z")
    zzs = JavaMethod("()Z")
    zzt = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    zzu = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    zzv = JavaMethod("()J")
    zzw = JavaMethod("(J)V")
    zzx = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    zzy = JavaMethod("()Lcom/google/android/gms/ads/VideoController;")
    zzz = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")
    zzA = JavaMethod("(Lcom/google/android/gms/ads/VideoOptions;)V")
    zzB = JavaMethod("()Lcom/google/android/gms/ads/VideoOptions;")
    zzC = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzbu;)Z")