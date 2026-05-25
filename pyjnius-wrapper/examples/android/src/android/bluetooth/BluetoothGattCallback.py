from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattCallback"]

class BluetoothGattCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattCallback"
    __javaconstructor__ = [("()V", False)]
    onPhyUpdate = JavaMethod("(Landroid/bluetooth/BluetoothGatt;III)V")
    onPhyRead = JavaMethod("(Landroid/bluetooth/BluetoothGatt;III)V")
    onConnectionStateChange = JavaMethod("(Landroid/bluetooth/BluetoothGatt;II)V")
    onServicesDiscovered = JavaMethod("(Landroid/bluetooth/BluetoothGatt;I)V")
    onCharacteristicRead = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;I)V", False, False), ("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;[BI)V", False, False)])
    onCharacteristicWrite = JavaMethod("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;I)V")
    onCharacteristicChanged = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;)V", False, False), ("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattCharacteristic;[B)V", False, False)])
    onDescriptorRead = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattDescriptor;I)V", False, False), ("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattDescriptor;I[B)V", False, False)])
    onDescriptorWrite = JavaMethod("(Landroid/bluetooth/BluetoothGatt;Landroid/bluetooth/BluetoothGattDescriptor;I)V")
    onReliableWriteCompleted = JavaMethod("(Landroid/bluetooth/BluetoothGatt;I)V")
    onReadRemoteRssi = JavaMethod("(Landroid/bluetooth/BluetoothGatt;II)V")
    onMtuChanged = JavaMethod("(Landroid/bluetooth/BluetoothGatt;II)V")
    onServiceChanged = JavaMethod("(Landroid/bluetooth/BluetoothGatt;)V")