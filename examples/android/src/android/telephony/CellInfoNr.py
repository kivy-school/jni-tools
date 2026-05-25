from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellInfoNr"]

class CellInfoNr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellInfoNr"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCellIdentity = JavaMethod("()Landroid/telephony/CellIdentity;")
    getCellSignalStrength = JavaMethod("()Landroid/telephony/CellSignalStrength;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")