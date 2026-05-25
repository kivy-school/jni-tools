from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzv"]

class zzv(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzv"
    __javaconstructor__ = [("(Ljava/lang/String;JLcom/google/android/gms/ads/internal/client/zze;Landroid/os/Bundle;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("J")
    zzc = JavaField("Lcom/google/android/gms/ads/internal/client/zze;")
    zzd = JavaField("Landroid/os/Bundle;")
    zze = JavaField("Ljava/lang/String;")
    zzf = JavaField("Ljava/lang/String;")
    zzg = JavaField("Ljava/lang/String;")
    zzh = JavaField("Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")