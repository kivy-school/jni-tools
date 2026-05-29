from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NeighboringCellInfo"]

class NeighboringCellInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/NeighboringCellInfo"
    __javaconstructor__ = [("()V", False), ("(II)V", False), ("(ILjava/lang/String;I)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UNKNOWN_CID = JavaStaticField("I")
    UNKNOWN_RSSI = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPsc = JavaMethod("()I")
    setCid = JavaMethod("(I)V")
    setRssi = JavaMethod("(I)V")
    getLac = JavaMethod("()I")
    getCid = JavaMethod("()I")
    getNetworkType = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getRssi = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")