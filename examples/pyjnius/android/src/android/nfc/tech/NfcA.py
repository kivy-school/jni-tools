from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcA"]

class NfcA(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcA"
    connect = JavaMethod("()V")
    getSak = JavaMethod("()S")
    getAtqa = JavaMethod("()[B")
    getTimeout = JavaMethod("()I")
    setTimeout = JavaMethod("(I)V")
    getMaxTransceiveLength = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    transceive = JavaMethod("([B)[B")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcA;")
    close = JavaMethod("()V")
    getTag = JavaMethod("()Landroid/nfc/Tag;")