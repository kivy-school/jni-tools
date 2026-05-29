from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NeighboringCellInfo"]

class NeighboringCellInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/NeighboringCellInfo"
    __javaconstructor__ = [("()V", False), ("(II)V", False), ("(ILjava/lang/String;I)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UNKNOWN_CID = JavaStaticField("I")
    UNKNOWN_RSSI = JavaStaticField("I")
    getRssi = JavaMethod("()I")
    getLac = JavaMethod("()I")
    getCid = JavaMethod("()I")
    getPsc = JavaMethod("()I")
    getNetworkType = JavaMethod("()I")
    setCid = JavaMethod("(I)V")
    setRssi = JavaMethod("(I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")