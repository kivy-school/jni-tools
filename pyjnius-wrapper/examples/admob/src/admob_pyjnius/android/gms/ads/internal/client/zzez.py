from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzez"]

class zzez(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzez"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    zza = JavaMethod("()I")
    zzb = JavaMethod("()Ljava/lang/String;")