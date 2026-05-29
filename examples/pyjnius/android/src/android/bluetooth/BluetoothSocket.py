from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothSocket"]

class BluetoothSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothSocket"
    TYPE_L2CAP = JavaStaticField("I")
    TYPE_LE = JavaStaticField("I")
    TYPE_RFCOMM = JavaStaticField("I")
    TYPE_SCO = JavaStaticField("I")
    connect = JavaMethod("()V")
    isConnected = JavaMethod("()Z")
    getRemoteDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")
    getConnectionType = JavaMethod("()I")
    getMaxReceivePacketSize = JavaMethod("()I")
    getMaxTransmitPacketSize = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")