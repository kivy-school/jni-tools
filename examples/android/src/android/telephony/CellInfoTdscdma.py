from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellInfoTdscdma"]

class CellInfoTdscdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellInfoTdscdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCellIdentity = JavaMethod("()Landroid/telephony/CellIdentityTdscdma;")
    getCellSignalStrength = JavaMethod("()Landroid/telephony/CellSignalStrengthTdscdma;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")