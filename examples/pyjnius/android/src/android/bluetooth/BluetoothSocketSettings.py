from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothSocketSettings"]

class BluetoothSocketSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothSocketSettings"
    isEncryptionRequired = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    isAuthenticationRequired = JavaMethod("()Z")
    getSocketType = JavaMethod("()I")
    getRfcommUuid = JavaMethod("()Ljava/util/UUID;")
    getL2capPsm = JavaMethod("()I")
    getRfcommServiceName = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/BluetoothSocketSettings$Builder"
        __javaconstructor__ = [("()V", False)]
        setL2capPsm = JavaMethod("(I)Landroid/bluetooth/BluetoothSocketSettings$Builder;")
        setRfcommUuid = JavaMethod("(Ljava/util/UUID;)Landroid/bluetooth/BluetoothSocketSettings$Builder;")
        setSocketType = JavaMethod("(I)Landroid/bluetooth/BluetoothSocketSettings$Builder;")
        setRfcommServiceName = JavaMethod("(Ljava/lang/String;)Landroid/bluetooth/BluetoothSocketSettings$Builder;")
        setAuthenticationRequired = JavaMethod("(Z)Landroid/bluetooth/BluetoothSocketSettings$Builder;")
        setEncryptionRequired = JavaMethod("(Z)Landroid/bluetooth/BluetoothSocketSettings$Builder;")
        build = JavaMethod("()Landroid/bluetooth/BluetoothSocketSettings;")