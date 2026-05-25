from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbyv"]

class zzbyv(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbyv"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd$OnCustomFormatAdLoadedListener;Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd$OnCustomClickListener;)V", False)]
    zza = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnp;")
    zzb = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnm;")