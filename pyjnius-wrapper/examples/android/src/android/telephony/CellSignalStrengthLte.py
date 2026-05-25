from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthLte"]

class CellSignalStrengthLte(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthLte"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLevel = JavaMethod("()I")
    getRsrq = JavaMethod("()I")
    getRssi = JavaMethod("()I")
    getRssnr = JavaMethod("()I")
    getRsrp = JavaMethod("()I")
    getCqiTableIndex = JavaMethod("()I")
    getCqi = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    getTimingAdvance = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")