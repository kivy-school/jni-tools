from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothLeAudioCodecStatus"]

class BluetoothLeAudioCodecStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothLeAudioCodecStatus"
    __javaconstructor__ = [("(Landroid/bluetooth/BluetoothLeAudioCodecConfig;Landroid/bluetooth/BluetoothLeAudioCodecConfig;Ljava/util/List;Ljava/util/List;Ljava/util/List;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_LE_AUDIO_CODEC_STATUS = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInputCodecConfig = JavaMethod("()Landroid/bluetooth/BluetoothLeAudioCodecConfig;")
    getInputCodecLocalCapabilities = JavaMethod("()Ljava/util/List;")
    getInputCodecSelectableCapabilities = JavaMethod("()Ljava/util/List;")
    getOutputCodecConfig = JavaMethod("()Landroid/bluetooth/BluetoothLeAudioCodecConfig;")
    getOutputCodecLocalCapabilities = JavaMethod("()Ljava/util/List;")
    getOutputCodecSelectableCapabilities = JavaMethod("()Ljava/util/List;")
    isInputCodecConfigSelectable = JavaMethod("(Landroid/bluetooth/BluetoothLeAudioCodecConfig;)Z")
    isOutputCodecConfigSelectable = JavaMethod("(Landroid/bluetooth/BluetoothLeAudioCodecConfig;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")