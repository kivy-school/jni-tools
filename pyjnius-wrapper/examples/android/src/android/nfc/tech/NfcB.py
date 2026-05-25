from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcB"]

class NfcB(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcB"
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcB;")
    getApplicationData = JavaMethod("()[B")
    getProtocolInfo = JavaMethod("()[B")
    transceive = JavaMethod("([B)[B")
    getMaxTransceiveLength = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")