from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbip"]

class zzbip(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbip"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbio;)V")
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbio;)V")
    zzc = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbio;)V")
    zzd = JavaMethod("(Landroid/content/SharedPreferences$Editor;ILorg/json/JSONObject;)V")
    zze = JavaMethod("()Ljava/util/List;")
    zzf = JavaMethod("()Ljava/util/List;")