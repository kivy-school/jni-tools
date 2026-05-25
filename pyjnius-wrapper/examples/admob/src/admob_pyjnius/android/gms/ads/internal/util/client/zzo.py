from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzo"]

class zzo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzo"
    zzb = JavaStaticField("Lcom/google/android/gms/internal/ads/zzgug;")
    zzd = JavaStaticMethod("(Ljava/lang/String;)V")
    zze = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    zzf = JavaStaticMethod("(Ljava/lang/String;)V")
    zzg = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    zzh = JavaStaticMethod("(Ljava/lang/String;)V")
    zzi = JavaStaticMethod("(Ljava/lang/String;)V")
    zzj = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    zzl = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/Throwable;)V")
    zzm = JavaStaticMethod("(I)Z")