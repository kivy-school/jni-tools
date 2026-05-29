from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzg"]

class zzg(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzg"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/AdListener;)V", False)]
    zzb = JavaMethod("()V")
    zzc = JavaMethod("(I)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("()V")
    zzh = JavaMethod("()V")
    zzi = JavaMethod("()V")
    zzj = JavaMethod("()V")
    zzk = JavaMethod("()Lcom/google/android/gms/ads/AdListener;")