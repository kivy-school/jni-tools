from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothServerSocket"]

class BluetoothServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothServerSocket"
    getPsm = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    accept = JavaMultipleMethod([("()Landroid/bluetooth/BluetoothSocket;", False, False), ("(I)Landroid/bluetooth/BluetoothSocket;", False, False)])