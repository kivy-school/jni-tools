from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothLeAudioCodecStatus"]

class BluetoothLeAudioCodecStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothLeAudioCodecStatus"
    __javaconstructor__ = [("(Landroid/bluetooth/BluetoothLeAudioCodecConfig;Landroid/bluetooth/BluetoothLeAudioCodecConfig;Ljava/util/List;Ljava/util/List;Ljava/util/List;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_LE_AUDIO_CODEC_STATUS = JavaStaticField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    isInputCodecConfigSelectable = JavaMethod("(Landroid/bluetooth/BluetoothLeAudioCodecConfig;)Z")
    isOutputCodecConfigSelectable = JavaMethod("(Landroid/bluetooth/BluetoothLeAudioCodecConfig;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getInputCodecConfig = JavaMethod("()Landroid/bluetooth/BluetoothLeAudioCodecConfig;")
    getOutputCodecConfig = JavaMethod("()Landroid/bluetooth/BluetoothLeAudioCodecConfig;")
    getInputCodecLocalCapabilities = JavaMethod("()Ljava/util/List;")
    getOutputCodecLocalCapabilities = JavaMethod("()Ljava/util/List;")
    getInputCodecSelectableCapabilities = JavaMethod("()Ljava/util/List;")
    getOutputCodecSelectableCapabilities = JavaMethod("()Ljava/util/List;")