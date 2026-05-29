from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcF"]

class NfcF(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcF"
    connect = JavaMethod("()V")
    getTimeout = JavaMethod("()I")
    setTimeout = JavaMethod("(I)V")
    getSystemCode = JavaMethod("()[B")
    getMaxTransceiveLength = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    transceive = JavaMethod("([B)[B")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcF;")
    close = JavaMethod("()V")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    getManufacturer = JavaMethod("()[B")