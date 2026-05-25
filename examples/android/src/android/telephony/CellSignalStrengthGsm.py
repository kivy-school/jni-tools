from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthGsm"]

class CellSignalStrengthGsm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthGsm"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLevel = JavaMethod("()I")
    getTimingAdvance = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    getRssi = JavaMethod("()I")
    getBitErrorRate = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")