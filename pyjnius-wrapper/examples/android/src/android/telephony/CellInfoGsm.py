from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellInfoGsm"]

class CellInfoGsm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellInfoGsm"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCellIdentity = JavaMethod("()Landroid/telephony/CellIdentityGsm;")
    getCellSignalStrength = JavaMethod("()Landroid/telephony/CellSignalStrengthGsm;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")