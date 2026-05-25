from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothLeAudio"]

class BluetoothLeAudio(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothLeAudio"
    ACTION_LE_AUDIO_CONNECTION_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    GROUP_ID_INVALID = JavaStaticField("I")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")
    getConnectedGroupLeadDevice = JavaMethod("(I)Landroid/bluetooth/BluetoothDevice;")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")
    getGroupId = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")