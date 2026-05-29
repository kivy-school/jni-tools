from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfp"]

class zzfp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfp"
    __javaconstructor__ = [("(Ljava/lang/String;ILcom/google/android/gms/ads/internal/client/zzm;IZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("I")
    zzc = JavaField("Lcom/google/android/gms/ads/internal/client/zzm;")
    zzd = JavaField("I")
    zze = JavaField("Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    zza = JavaMethod("(I)Lcom/google/android/gms/ads/internal/client/zzfp;")