from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzl"]

class zzl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzl"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
    zza = JavaMethod("(Ljava/net/HttpURLConnection;[B)V")
    zzb = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;[B)V")
    zzc = JavaMethod("(Ljava/net/HttpURLConnection;I)V")
    zzd = JavaMethod("(Ljava/util/Map;I)V")
    zze = JavaMethod("(Ljava/lang/String;)V")
    zzf = JavaMethod("([B)V")
    zzg = JavaStaticMethod("()V")
    zzh = JavaStaticMethod("(Z)V")
    zzi = JavaStaticMethod("()Z")
    zzj = JavaStaticMethod("()Z")