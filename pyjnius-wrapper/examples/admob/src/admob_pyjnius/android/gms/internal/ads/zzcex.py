from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcex"]

class zzcex(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcex"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Lcom/google/android/gms/ads/internal/client/zzr;Lcom/google/android/gms/ads/internal/client/zzm;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("Ljava/lang/String;")
    zzc = JavaField("Lcom/google/android/gms/ads/internal/client/zzr;")
    zzd = JavaField("Lcom/google/android/gms/ads/internal/client/zzm;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")