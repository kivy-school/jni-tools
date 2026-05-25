from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfw"]

class zzfw(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfw"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/VideoOptions;)V", False), ("(ZZZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("Z")
    zzb = JavaField("Z")
    zzc = JavaField("Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")