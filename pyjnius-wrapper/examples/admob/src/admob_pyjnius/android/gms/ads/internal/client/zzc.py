from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzc"]

class zzc(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzc"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Ljava/lang/String;")
    zzb = JavaField("Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")