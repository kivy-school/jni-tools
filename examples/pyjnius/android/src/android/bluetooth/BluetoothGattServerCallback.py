from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattServerCallback"]

class BluetoothGattServerCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattServerCallback"
    __javaconstructor__ = [("()V", False)]
    onMtuChanged = JavaMethod("(Landroid/bluetooth/BluetoothDevice;I)V")
    onCharacteristicReadRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;IILandroid/bluetooth/BluetoothGattCharacteristic;)V")
    onExecuteWrite = JavaMethod("(Landroid/bluetooth/BluetoothDevice;IZ)V")
    onCharacteristicWriteRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;ILandroid/bluetooth/BluetoothGattCharacteristic;ZZI[B)V")
    onConnectionStateChange = JavaMethod("(Landroid/bluetooth/BluetoothDevice;II)V")
    onDescriptorReadRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;IILandroid/bluetooth/BluetoothGattDescriptor;)V")
    onDescriptorWriteRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;ILandroid/bluetooth/BluetoothGattDescriptor;ZZI[B)V")
    onNotificationSent = JavaMethod("(Landroid/bluetooth/BluetoothDevice;I)V")
    onPhyRead = JavaMethod("(Landroid/bluetooth/BluetoothDevice;III)V")
    onPhyUpdate = JavaMethod("(Landroid/bluetooth/BluetoothDevice;III)V")
    onServiceAdded = JavaMethod("(ILandroid/bluetooth/BluetoothGattService;)V")