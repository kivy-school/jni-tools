from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpSecTransformState"]

class IpSecTransformState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpSecTransformState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getTimestampMillis = JavaMethod("()J")
    getTxHighestSequenceNumber = JavaMethod("()J")
    getRxHighestSequenceNumber = JavaMethod("()J")
    getPacketCount = JavaMethod("()J")
    getByteCount = JavaMethod("()J")
    getReplayBitmap = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecTransformState/Builder"
        __javaconstructor__ = [("()V", False)]
        setTimestampMillis = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setTxHighestSequenceNumber = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setRxHighestSequenceNumber = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setPacketCount = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setByteCount = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setReplayBitmap = JavaMethod("([B)Landroid/net/IpSecTransformState$Builder;")
        build = JavaMethod("()Landroid/net/IpSecTransformState;")