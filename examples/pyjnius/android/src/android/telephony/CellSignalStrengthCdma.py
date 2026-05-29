from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthCdma"]

class CellSignalStrengthCdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthCdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLevel = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    getCdmaLevel = JavaMethod("()I")
    getEvdoLevel = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getCdmaDbm = JavaMethod("()I")
    getCdmaEcio = JavaMethod("()I")
    getEvdoDbm = JavaMethod("()I")
    getEvdoEcio = JavaMethod("()I")
    getEvdoSnr = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")