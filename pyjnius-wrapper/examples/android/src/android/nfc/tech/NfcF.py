from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcF"]

class NfcF(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcF"
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcF;")
    getSystemCode = JavaMethod("()[B")
    getManufacturer = JavaMethod("()[B")
    transceive = JavaMethod("([B)[B")
    getMaxTransceiveLength = JavaMethod("()I")
    setTimeout = JavaMethod("(I)V")
    getTimeout = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")