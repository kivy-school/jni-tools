from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzr"]

class zzr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzr"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Lcom/google/android/gms/ads/AdSize;)V", False), ("(Landroid/content/Context;[Lcom/google/android/gms/ads/AdSize;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("I")
    zzc = JavaField("I")
    zzd = JavaField("Z")
    zze = JavaField("I")
    zzf = JavaField("I")
    zzg = JavaField("[Lcom/google/android/gms/ads/internal/client/zzr;")
    zzh = JavaField("Z")
    zzi = JavaField("Z")
    zzj = JavaField("Z")
    zzk = JavaField("Z")
    zzl = JavaField("Z")
    zzm = JavaField("Z")
    zzn = JavaField("Z")
    zzo = JavaField("Z")
    zzp = JavaField("Z")
    zza = JavaStaticMethod("(Landroid/util/DisplayMetrics;)I")
    zzb = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/client/zzr;")
    zzc = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/client/zzr;")
    zzd = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/client/zzr;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")