from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHearingAid"]

class BluetoothHearingAid(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHearingAid"
    ACTION_CONNECTION_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")