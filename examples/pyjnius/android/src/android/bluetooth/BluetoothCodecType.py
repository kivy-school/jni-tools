from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isMandatoryCodec = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getCodecId = JavaMethod("()J")
    getCodecName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")