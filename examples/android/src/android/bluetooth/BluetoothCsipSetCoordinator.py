from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothCsipSetCoordinator"]

class BluetoothCsipSetCoordinator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothCsipSetCoordinator"
    ACTION_CSIS_CONNECTION_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    finalize = JavaMethod("()V")
    close = JavaMethod("()V")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")