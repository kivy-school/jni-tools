from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbrw"]

class zzbrw(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbrw"
    __javaconstructor__ = [("(Ljava/lang/String;ZILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("Z")
    zzc = JavaField("I")
    zzd = JavaField("Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")