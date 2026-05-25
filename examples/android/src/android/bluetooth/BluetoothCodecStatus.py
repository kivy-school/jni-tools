from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothCodecStatus"]

class BluetoothCodecStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothCodecStatus"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_CODEC_STATUS = JavaStaticField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    isCodecConfigSelectable = JavaMethod("(Landroid/bluetooth/BluetoothCodecConfig;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCodecConfig = JavaMethod("()Landroid/bluetooth/BluetoothCodecConfig;")
    getCodecsLocalCapabilities = JavaMethod("()Ljava/util/List;")
    getCodecsSelectableCapabilities = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/BluetoothCodecStatus/Builder"
        __javaconstructor__ = [("()V", False)]
        setCodecConfig = JavaMethod("(Landroid/bluetooth/BluetoothCodecConfig;)Landroid/bluetooth/BluetoothCodecStatus$Builder;")
        setCodecsLocalCapabilities = JavaMethod("(Ljava/util/List;)Landroid/bluetooth/BluetoothCodecStatus$Builder;")
        setCodecsSelectableCapabilities = JavaMethod("(Ljava/util/List;)Landroid/bluetooth/BluetoothCodecStatus$Builder;")
        build = JavaMethod("()Landroid/bluetooth/BluetoothCodecStatus;")