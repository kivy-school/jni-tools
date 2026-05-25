from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellInfoCdma"]

class CellInfoCdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellInfoCdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCellIdentity = JavaMethod("()Landroid/telephony/CellIdentityCdma;")
    getCellSignalStrength = JavaMethod("()Landroid/telephony/CellSignalStrengthCdma;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")