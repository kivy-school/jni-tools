from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHealthCallback"]

class BluetoothHealthCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHealthCallback"
    __javaconstructor__ = [("()V", False)]
    onHealthAppConfigurationStatusChange = JavaMethod("(Landroid/bluetooth/BluetoothHealthAppConfiguration;I)V")
    onHealthChannelStateChange = JavaMethod("(Landroid/bluetooth/BluetoothHealthAppConfiguration;Landroid/bluetooth/BluetoothDevice;IILandroid/os/ParcelFileDescriptor;I)V")