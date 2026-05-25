from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfr"]

class zzfr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfr"
    __javaconstructor__ = [("(II)V", False), ("(Lcom/google/android/gms/ads/RequestConfiguration;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("I")
    zzb = JavaField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")