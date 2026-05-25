from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbgl"]

class zzbgl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbgl"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/appopen/AppOpenAd$AppOpenAdLoadCallback;Ljava/lang/String;)V", False)]
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbgq;)V")
    zzc = JavaMethod("(I)V")
    zzd = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")