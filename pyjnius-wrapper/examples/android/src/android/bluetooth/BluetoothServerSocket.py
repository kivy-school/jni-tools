from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothServerSocket"]

class BluetoothServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothServerSocket"
    accept = JavaMultipleMethod([("()Landroid/bluetooth/BluetoothSocket;", False, False), ("(I)Landroid/bluetooth/BluetoothSocket;", False, False)])
    close = JavaMethod("()V")
    getPsm = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")