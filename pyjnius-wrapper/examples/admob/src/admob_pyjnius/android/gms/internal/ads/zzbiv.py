from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbiv"]

class zzbiv(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbiv"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Landroid/content/Context;)V")
    zzc = JavaMethod("()Z")
    zzd = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbio;)Ljava/lang/Object;")
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbio;)Ljava/lang/Object;")
    onSharedPreferenceChanged = JavaMethod("(Landroid/content/SharedPreferences;Ljava/lang/String;)V")