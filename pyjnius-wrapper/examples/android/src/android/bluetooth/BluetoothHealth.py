from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHealth"]

class BluetoothHealth(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHealth"
    APP_CONFIG_REGISTRATION_FAILURE = JavaStaticField("I")
    APP_CONFIG_REGISTRATION_SUCCESS = JavaStaticField("I")
    APP_CONFIG_UNREGISTRATION_FAILURE = JavaStaticField("I")
    APP_CONFIG_UNREGISTRATION_SUCCESS = JavaStaticField("I")
    CHANNEL_TYPE_RELIABLE = JavaStaticField("I")
    CHANNEL_TYPE_STREAMING = JavaStaticField("I")
    SINK_ROLE = JavaStaticField("I")
    SOURCE_ROLE = JavaStaticField("I")
    STATE_CHANNEL_CONNECTED = JavaStaticField("I")
    STATE_CHANNEL_CONNECTING = JavaStaticField("I")
    STATE_CHANNEL_DISCONNECTED = JavaStaticField("I")
    STATE_CHANNEL_DISCONNECTING = JavaStaticField("I")
    registerSinkAppConfiguration = JavaMethod("(Ljava/lang/String;ILandroid/bluetooth/BluetoothHealthCallback;)Z")
    unregisterAppConfiguration = JavaMethod("(Landroid/bluetooth/BluetoothHealthAppConfiguration;)Z")
    connectChannelToSource = JavaMethod("(Landroid/bluetooth/BluetoothDevice;Landroid/bluetooth/BluetoothHealthAppConfiguration;)Z")
    disconnectChannel = JavaMethod("(Landroid/bluetooth/BluetoothDevice;Landroid/bluetooth/BluetoothHealthAppConfiguration;I)Z")
    getMainChannelFd = JavaMethod("(Landroid/bluetooth/BluetoothDevice;Landroid/bluetooth/BluetoothHealthAppConfiguration;)Landroid/os/ParcelFileDescriptor;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")