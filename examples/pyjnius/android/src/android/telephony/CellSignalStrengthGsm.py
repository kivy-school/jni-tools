from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthGsm"]

class CellSignalStrengthGsm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthGsm"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    SIGNAL_STRENGTH_GOOD = JavaStaticField("I")
    SIGNAL_STRENGTH_GREAT = JavaStaticField("I")
    SIGNAL_STRENGTH_MODERATE = JavaStaticField("I")
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN = JavaStaticField("I")
    SIGNAL_STRENGTH_POOR = JavaStaticField("I")
    getTimingAdvance = JavaMethod("()I")
    getBitErrorRate = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getRssi = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getLevel = JavaMethod("()I")