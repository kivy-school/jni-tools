from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattCallback"]

class BluetoothGattCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattCallback"
    __javaconstructor__ = [("()V", False)]
    onDescriptorWrite = JavaMethod("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattDescriptor;I)V")
    onReadRemoteRssi = JavaMethod("(Landroid/bluetooth/BluetoothGatt;II)V")
    onCharacteristicChanged = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;[B)V", False, False), ("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;)V", False, False)])
    onCharacteristicRead = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;I)V", False, False), ("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;[BI)V", False, False)])
    onServiceChanged = JavaMethod("(Landroid/bluetooth/BluetoothGatt;)V")
    onCharacteristicWrite = JavaMethod("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;I)V")
    onDescriptorRead = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattDescriptor;I[B)V", False, False), ("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattDescriptor;I)V", False, False)])
    onReliableWriteCompleted = JavaMethod("(Landroid/bluetooth/BluetoothGatt;I)V")
    onServicesDiscovered = JavaMethod("(Landroid/bluetooth/BluetoothGatt;I)V")
    onMtuChanged = JavaMethod("(Landroid/bluetooth/BluetoothGatt;II)V")
    onConnectionStateChange = JavaMethod("(Landroid/bluetooth/BluetoothGatt;II)V")
    onPhyRead = JavaMethod("(Landroid/bluetooth/BluetoothGatt;III)V")
    onPhyUpdate = JavaMethod("(Landroid/bluetooth/BluetoothGatt;III)V")