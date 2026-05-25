from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zze"]

class zze(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zze"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;Lcom/google/android/gms/ads/internal/client/zze;Landroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("I")
    zzb = JavaField("Ljava/lang/String;")
    zzc = JavaField("Ljava/lang/String;")
    zzd = JavaField("Lcom/google/android/gms/ads/internal/client/zze;")
    zze = JavaField("Landroid/os/IBinder;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    zza = JavaMethod("()Lcom/google/android/gms/ads/AdError;")
    zzb = JavaMethod("()Lcom/google/android/gms/ads/LoadAdError;")