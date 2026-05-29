from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcdh"]

class zzcdh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcdh"
    __javaconstructor__ = [("()V", False)]
    zzb = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    zzc = JavaMethod("(Lcom/google/android/gms/ads/OnUserEarnedRewardListener;)V")
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")
    zzh = JavaMethod("(I)V")
    zzi = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zzg = JavaMethod("(Lcom/google/android/gms/internal/ads/zzccm;)V")
    zzj = JavaMethod("()V")
    zzk = JavaMethod("()V")