from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzx"]

class zzx(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzx"
    __javaconstructor__ = [("(I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    zza = JavaField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")