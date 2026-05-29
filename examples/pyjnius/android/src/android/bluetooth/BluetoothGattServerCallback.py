from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattServerCallback"]

class BluetoothGattServerCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattServerCallback"
    __javaconstructor__ = [("()V", False)]
    onConnectionStateChange = JavaMethod("(Landroid/bluetooth/BluetoothDevice;II)V")
    onServiceAdded = JavaMethod("(ILandroid/bluetooth/BluetoothGattService;)V")
    onCharacteristicReadRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;IILandroid/bluetooth/BluetoothGattCharacteristic;)V")
    onCharacteristicWriteRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;ILandroid/bluetooth/BluetoothGattCharacteristic;ZZI[B)V")
    onDescriptorReadRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;IILandroid/bluetooth/BluetoothGattDescriptor;)V")
    onDescriptorWriteRequest = JavaMethod("(Landroid/bluetooth/BluetoothDevice;ILandroid/bluetooth/BluetoothGattDescriptor;ZZI[B)V")
    onExecuteWrite = JavaMethod("(Landroid/bluetooth/BluetoothDevice;IZ)V")
    onNotificationSent = JavaMethod("(Landroid/bluetooth/BluetoothDevice;I)V")
    onMtuChanged = JavaMethod("(Landroid/bluetooth/BluetoothDevice;I)V")
    onPhyUpdate = JavaMethod("(Landroid/bluetooth/BluetoothDevice;III)V")
    onPhyRead = JavaMethod("(Landroid/bluetooth/BluetoothDevice;III)V")