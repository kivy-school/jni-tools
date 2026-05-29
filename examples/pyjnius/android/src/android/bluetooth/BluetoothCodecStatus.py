from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothCodecStatus"]

class BluetoothCodecStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothCodecStatus"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_CODEC_STATUS = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCodecsLocalCapabilities = JavaMethod("()Ljava/util/List;")
    getCodecsSelectableCapabilities = JavaMethod("()Ljava/util/List;")
    isCodecConfigSelectable = JavaMethod("(Landroid/bluetooth/BluetoothCodecConfig;)Z")
    getCodecConfig = JavaMethod("()Landroid/bluetooth/BluetoothCodecConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/BluetoothCodecStatus$Builder"
        __javaconstructor__ = [("()V", False)]
        setCodecsLocalCapabilities = JavaMethod("(Ljava/util/List;)Landroid/bluetooth/BluetoothCodecStatus$Builder;")
        setCodecsSelectableCapabilities = JavaMethod("(Ljava/util/List;)Landroid/bluetooth/BluetoothCodecStatus$Builder;")
        setCodecConfig = JavaMethod("(Landroid/bluetooth/BluetoothCodecConfig;)Landroid/bluetooth/BluetoothCodecStatus$Builder;")
        build = JavaMethod("()Landroid/bluetooth/BluetoothCodecStatus;")