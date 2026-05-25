from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothCodecType"]

class BluetoothCodecType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothCodecType"
    CODEC_ID_AAC = JavaStaticField("J")
    CODEC_ID_APTX = JavaStaticField("J")
    CODEC_ID_APTX_HD = JavaStaticField("J")
    CODEC_ID_LDAC = JavaStaticField("J")
    CODEC_ID_OPUS = JavaStaticField("J")
    CODEC_ID_SBC = JavaStaticField("J")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isMandatoryCodec = JavaMethod("()Z")
    getCodecId = JavaMethod("()J")
    getCodecName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")