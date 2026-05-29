from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbgn"]

class zzbgn(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbgn"
    __javaconstructor__ = [("()V", False)]
    zzb = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    zzc = JavaMethod("()V")
    zzd = JavaMethod("()V")
    zze = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("()V")