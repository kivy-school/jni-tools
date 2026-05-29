from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzeg"]

class zzeg(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzeg"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Ljava/lang/String;)V")
    zzb = JavaMethod("(Landroid/os/Bundle;)V")
    zzc = JavaMethod("(Ljava/lang/Class;Landroid/os/Bundle;)V")
    zzd = JavaMethod("(Ljava/lang/Class;Landroid/os/Bundle;)V")
    zze = JavaMethod("(Ljava/lang/String;)V")
    zzf = JavaMethod("(Ljava/lang/String;)V")
    zzg = JavaMethod("(Ljava/lang/String;)V")
    zzh = JavaMethod("(Ljava/util/List;)V")
    zzi = JavaMethod("(Ljava/lang/String;)V")
    zzj = JavaMethod("(Ljava/lang/String;)V")
    zzk = JavaMethod("(Z)V")
    zzl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    zzm = JavaMethod("(Ljava/lang/String;)V")
    zzn = JavaMethod("(Z)V")
    zzo = JavaMethod("(Ljava/lang/String;)V")
    zzp = JavaMethod("(I)V")
    zzq = JavaMethod("(J)V")