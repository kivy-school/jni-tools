from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcV"]

class NfcV(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcV"
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcV;")
    getResponseFlags = JavaMethod("()B")
    getDsfId = JavaMethod("()B")
    transceive = JavaMethod("([B)[B")
    getMaxTransceiveLength = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")