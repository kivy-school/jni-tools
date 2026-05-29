from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothLeAudio"]

class BluetoothLeAudio(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothLeAudio"
    ACTION_LE_AUDIO_CONNECTION_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    GROUP_ID_INVALID = JavaStaticField("I")
    A2DP = JavaStaticField("I")
    CSIP_SET_COORDINATOR = JavaStaticField("I")
    EXTRA_PREVIOUS_STATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_STATE = JavaStaticField("Ljava/lang/String;")
    GATT = JavaStaticField("I")
    GATT_SERVER = JavaStaticField("I")
    HAP_CLIENT = JavaStaticField("I")
    HEADSET = JavaStaticField("I")
    HEALTH = JavaStaticField("I")
    HEARING_AID = JavaStaticField("I")
    HID_DEVICE = JavaStaticField("I")
    LE_AUDIO = JavaStaticField("I")
    SAP = JavaStaticField("I")
    STATE_CONNECTED = JavaStaticField("I")
    STATE_CONNECTING = JavaStaticField("I")
    STATE_DISCONNECTED = JavaStaticField("I")
    STATE_DISCONNECTING = JavaStaticField("I")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")
    getConnectedGroupLeadDevice = JavaMethod("(I)Landroid/bluetooth/BluetoothDevice;")
    close = JavaMethod("()V")
    getGroupId = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")