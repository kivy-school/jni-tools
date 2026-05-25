from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzeh"]

class zzeh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzeh"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/internal/client/zzeg;)V", False)]
    zza = JavaMethod("()Ljava/lang/String;")
    zzb = JavaMethod("()Ljava/util/List;")
    zzc = JavaMethod("()Ljava/util/Set;")
    zzd = JavaMethod("(Ljava/lang/Class;)Landroid/os/Bundle;")
    zze = JavaMethod("(Ljava/lang/Class;)Landroid/os/Bundle;")
    zzf = JavaMethod("()Ljava/lang/String;")
    zzg = JavaMethod("()Ljava/lang/String;")
    zzh = JavaMethod("(Landroid/content/Context;)Z")
    zzi = JavaMethod("()Landroid/os/Bundle;")
    zzj = JavaMethod("()I")
    zzk = JavaMethod("()Landroid/os/Bundle;")
    zzl = JavaMethod("()Ljava/util/Set;")
    zzm = JavaMethod("()Z")
    zzn = JavaMethod("()Ljava/lang/String;")
    zzo = JavaMethod("()I")
    zzp = JavaMethod("(J)V")
    zzq = JavaMethod("()J")
    zzr = JavaMethod("()J")