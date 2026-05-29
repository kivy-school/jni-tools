from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHeadset"]

class BluetoothHeadset(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHeadset"
    ACTION_AUDIO_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_CONNECTION_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_VENDOR_SPECIFIC_HEADSET_EVENT = JavaStaticField("Ljava/lang/String;")
    AT_CMD_TYPE_ACTION = JavaStaticField("I")
    AT_CMD_TYPE_BASIC = JavaStaticField("I")
    AT_CMD_TYPE_READ = JavaStaticField("I")
    AT_CMD_TYPE_SET = JavaStaticField("I")
    AT_CMD_TYPE_TEST = JavaStaticField("I")
    EXTRA_VENDOR_SPECIFIC_HEADSET_EVENT_ARGS = JavaStaticField("Ljava/lang/String;")
    EXTRA_VENDOR_SPECIFIC_HEADSET_EVENT_CMD = JavaStaticField("Ljava/lang/String;")
    EXTRA_VENDOR_SPECIFIC_HEADSET_EVENT_CMD_TYPE = JavaStaticField("Ljava/lang/String;")
    STATE_AUDIO_CONNECTED = JavaStaticField("I")
    STATE_AUDIO_CONNECTING = JavaStaticField("I")
    STATE_AUDIO_DISCONNECTED = JavaStaticField("I")
    VENDOR_RESULT_CODE_COMMAND_ANDROID = JavaStaticField("Ljava/lang/String;")
    VENDOR_SPECIFIC_HEADSET_EVENT_COMPANY_ID_CATEGORY = JavaStaticField("Ljava/lang/String;")
    finalize = JavaMethod("()V")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")
    isNoiseReductionSupported = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)Z")
    isVoiceRecognitionSupported = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)Z")
    startVoiceRecognition = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)Z")
    stopVoiceRecognition = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)Z")
    isAudioConnected = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)Z")
    sendVendorSpecificResultCode = JavaMethod("(Landroid/bluetooth/BluetoothDevice;Ljava/lang/String;Ljava/lang/String;)Z")