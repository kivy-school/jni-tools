from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgtr"]

class zzgtr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgtr"
    zza = JavaStaticMethod("(Z)V")
    zzb = JavaStaticMethod("(ZLjava/lang/Object;)V")
    zzc = JavaStaticMethod("(ZLjava/lang/String;C)V")
    zzd = JavaStaticMethod("(ZLjava/lang/String;I)V")
    zze = JavaStaticMethod("(ZLjava/lang/String;J)V")
    zzf = JavaStaticMethod("(ZLjava/lang/String;Ljava/lang/Object;)V")
    zzg = JavaStaticMethod("(ZLjava/lang/String;II)V")
    zzh = JavaStaticMethod("(ZLjava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)V")
    zzi = JavaStaticMethod("(Z)V")
    zzj = JavaStaticMethod("(ZLjava/lang/Object;)V")
    zzk = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    zzl = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/Object;")
    zzm = JavaStaticMethod("(IILjava/lang/String;)I")
    zzn = JavaStaticMethod("(IILjava/lang/String;)I")
    zzo = JavaStaticMethod("(III)V")