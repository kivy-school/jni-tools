from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellSignalStrengthTdscdma"]

class CellSignalStrengthTdscdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellSignalStrengthTdscdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLevel = JavaMethod("()I")
    getDbm = JavaMethod("()I")
    getRscp = JavaMethod("()I")
    getAsuLevel = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")