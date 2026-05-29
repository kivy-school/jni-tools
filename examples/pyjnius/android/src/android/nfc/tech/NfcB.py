from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcB"]

class NfcB(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcB"
    connect = JavaMethod("()V")
    getMaxTransceiveLength = JavaMethod("()I")
    getProtocolInfo = JavaMethod("()[B")
    isConnected = JavaMethod("()Z")
    transceive = JavaMethod("([B)[B")
    getApplicationData = JavaMethod("()[B")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcB;")
    close = JavaMethod("()V")
    getTag = JavaMethod("()Landroid/nfc/Tag;")