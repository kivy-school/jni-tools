from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothA2dp"]

class BluetoothA2dp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothA2dp"
    ACTION_CONNECTION_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_PLAYING_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    STATE_NOT_PLAYING = JavaStaticField("I")
    STATE_PLAYING = JavaStaticField("I")
    finalize = JavaMethod("()V")
    getConnectedDevices = JavaMethod("()Ljava/util/List;")
    getDevicesMatchingConnectionStates = JavaMethod("([I)Ljava/util/List;")
    getConnectionState = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)I")
    isA2dpPlaying = JavaMethod("(Landroid/bluetooth/BluetoothDevice;)Z")
    getSupportedCodecTypes = JavaMethod("()Ljava/util/Collection;")