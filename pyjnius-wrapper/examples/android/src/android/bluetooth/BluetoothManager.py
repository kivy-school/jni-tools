from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothManager"]

class BluetoothManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothManager"
    getAdapter = JavaMethod("()Landroid/bluetooth/BluetoothAdapter;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;I)I")
    getConnectedDevices = JavaMethod("(I)Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("(I[I)Ljava/util/List;")
    openGattServer = JavaMethod("(Landroid/content/Context;Landroid/bluetooth/BluetoothGattServerCallback;)Landroid/bluetooth/BluetoothGattServer;")