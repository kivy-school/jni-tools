from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellInfoWcdma"]

class CellInfoWcdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellInfoWcdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCellIdentity = JavaMethod("()Landroid/telephony/CellIdentityWcdma;")
    getCellSignalStrength = JavaMethod("()Landroid/telephony/CellSignalStrengthWcdma;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")