from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattServer"]

class BluetoothGattServer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattServer"
    close = JavaMethod("()V")
    connect = JavaMethod("(Landroid/bluetooth/BluetoothDevice;Z)Z")
    cancelConnection = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)V")
    setPreferredPhy = JavaMethod("(Landroid/bluetooth/BluetoothDevice;III)V")
    readPhy = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)V")
    sendResponse = JavaMethod("(Landroid/bluetooth/BluetoothDevice;III[B)Z")
    notifyCharacteristicChanged = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothDevice;Landroid/bluetooth/BluetoothGattCharacteristic;Z)Z", False, False), ("(Landroid/bluetooth/BluetoothDevice;Landroid/bluetooth/BluetoothGattCharacteristic;Z[B)I", False, False)])
    addService = JavaMethod("(Landroid/bluetooth/BluetoothGattService;)Z")
    removeService = JavaMethod("(Landroid/bluetooth/BluetoothGattService;)Z")
    clearServices = JavaMethod("()V")
    getServices = JavaMethod("()Ljava/util/List;")
    getService = JavaMethod("(Ljava/util/UUID;)Landroid/bluetooth/BluetoothGattService;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")