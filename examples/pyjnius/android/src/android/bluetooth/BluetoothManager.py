from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothManager"]

class BluetoothManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothManager"
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;I)I")
    openGattServer = JavaMethod("(Landroid/content/Context;Landroid/bluetooth/BluetoothGattServerCallback;)Landroid/bluetooth/BluetoothGattServer;")
    getConnectedDevices = JavaMethod("(I)Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("(I[I)Ljava/util/List;")
    getAdapter = JavaMethod("()Landroid/bluetooth/BluetoothAdapter;")