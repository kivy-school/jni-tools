from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpSecTransformState"]

class IpSecTransformState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpSecTransformState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getReplayBitmap = JavaMethod("()[B")
    getPacketCount = JavaMethod("()J")
    getRxHighestSequenceNumber = JavaMethod("()J")
    getTxHighestSequenceNumber = JavaMethod("()J")
    getByteCount = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTimestampMillis = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecTransformState$Builder"
        __javaconstructor__ = [("()V", False)]
        setByteCount = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setReplayBitmap = JavaMethod("([B)Landroid/net/IpSecTransformState$Builder;")
        setPacketCount = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setRxHighestSequenceNumber = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setTxHighestSequenceNumber = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        setTimestampMillis = JavaMethod("(J)Landroid/net/IpSecTransformState$Builder;")
        build = JavaMethod("()Landroid/net/IpSecTransformState;")