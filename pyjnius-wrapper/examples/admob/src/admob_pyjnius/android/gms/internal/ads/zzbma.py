from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbma"]

class zzbma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbma"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/formats/NativeAdOptions;)V", False), ("(IZIZILcom/google/android/gms/ads/internal/client/zzfw;ZIIZI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("I")
    zzb = JavaField("Z")
    zzc = JavaField("I")
    zzd = JavaField("Z")
    zze = JavaField("I")
    zzf = JavaField("Lcom/google/android/gms/ads/internal/client/zzfw;")
    zzg = JavaField("Z")
    zzh = JavaField("I")
    zzi = JavaField("I")
    zzj = JavaField("Z")
    zzk = JavaField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    zza = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzbma;)Lcom/google/android/gms/ads/nativead/NativeAdOptions;")