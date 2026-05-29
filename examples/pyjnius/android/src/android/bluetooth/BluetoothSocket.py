from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothSocket"]

class BluetoothSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothSocket"
    TYPE_L2CAP = JavaStaticField("I")
    TYPE_RFCOMM = JavaStaticField("I")
    TYPE_SCO = JavaStaticField("I")
    finalize = JavaMethod("()V")
    getRemoteDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    isConnected = JavaMethod("()Z")
    connect = JavaMethod("()V")
    close = JavaMethod("()V")
    getMaxTransmitPacketSize = JavaMethod("()I")
    getMaxReceivePacketSize = JavaMethod("()I")
    getConnectionType = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")