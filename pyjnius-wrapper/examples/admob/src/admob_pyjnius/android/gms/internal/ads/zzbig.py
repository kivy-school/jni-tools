from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbig"]

class zzbig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbig"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Landroid/content/Context;)V")
    onSharedPreferenceChanged = JavaMethod("(Landroid/content/SharedPreferences;Ljava/lang/String;)V")
    zzb = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    zzc = JavaMethod("(Ljava/lang/String;J)J")
    zzd = JavaMethod("(Ljava/lang/String;I)I")
    zze = JavaMethod("(Ljava/lang/String;F)F")
    zzf = JavaMethod("(Ljava/lang/String;Z)Z")