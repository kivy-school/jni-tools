from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbio"]

class zzbio(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbio"
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Ljava/lang/Object;")
    zzg = JavaMethod("()Ljava/lang/Object;")
    zzh = JavaStaticMethod("(ILjava/lang/String;II)Lcom/google/android/gms/internal/ads/zzbio;")
    zzi = JavaStaticMethod("(ILjava/lang/String;JJ)Lcom/google/android/gms/internal/ads/zzbio;")
    zzj = JavaStaticMethod("(ILjava/lang/String;FF)Lcom/google/android/gms/internal/ads/zzbio;")
    zzk = JavaStaticMethod("(ILjava/lang/String;)Lcom/google/android/gms/internal/ads/zzbio;")
    zzl = JavaStaticMethod("(ILjava/lang/String;)Lcom/google/android/gms/internal/ads/zzbio;")
    zzm = JavaMethod("()I")
    zzd = JavaMethod("(Landroid/content/SharedPreferences;)Ljava/lang/Object;")
    zzc = JavaMethod("(Lorg/json/JSONObject;)Ljava/lang/Object;")
    zzb = JavaMethod("(Landroid/content/SharedPreferences$Editor;Ljava/lang/Object;)V")
    zza = JavaMethod("(Landroid/os/Bundle;)Ljava/lang/Object;")