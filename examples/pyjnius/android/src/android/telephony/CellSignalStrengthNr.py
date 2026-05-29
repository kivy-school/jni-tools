from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthNr"]

class CellSignalStrengthNr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthNr"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSsRsrp = JavaMethod("()I")
    getSsRsrq = JavaMethod("()I")
    getSsSinr = JavaMethod("()I")
    getCsiRsrp = JavaMethod("()I")
    getCsiRsrq = JavaMethod("()I")
    getCsiSinr = JavaMethod("()I")
    getCsiCqiTableIndex = JavaMethod("()I")
    getCsiCqiReport = JavaMethod("()Ljava/util/List;")
    getTimingAdvanceMicros = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getLevel = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")