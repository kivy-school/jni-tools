from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbsi"]

class zzbsi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbsi"
    __javaconstructor__ = [("(IILjava/lang/String;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("I")
    zzb = JavaField("I")
    zzc = JavaField("Ljava/lang/String;")
    zzd = JavaField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")