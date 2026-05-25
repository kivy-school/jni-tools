from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthWcdma"]

class CellSignalStrengthWcdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthWcdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLevel = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    getEcNo = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")