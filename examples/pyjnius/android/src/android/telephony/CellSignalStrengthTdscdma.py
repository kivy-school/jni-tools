from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthTdscdma"]

class CellSignalStrengthTdscdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthTdscdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    SIGNAL_STRENGTH_GOOD = JavaStaticField("I")
    SIGNAL_STRENGTH_GREAT = JavaStaticField("I")
    SIGNAL_STRENGTH_MODERATE = JavaStaticField("I")
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN = JavaStaticField("I")
    SIGNAL_STRENGTH_POOR = JavaStaticField("I")
    getRscp = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getLevel = JavaMethod("()I")