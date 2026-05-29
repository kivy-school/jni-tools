from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcV"]

class NfcV(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcV"
    connect = JavaMethod("()V")
    getResponseFlags = JavaMethod("()B")
    getDsfId = JavaMethod("()B")
    getMaxTransceiveLength = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    transceive = JavaMethod("([B)[B")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcV;")
    close = JavaMethod("()V")
    getTag = JavaMethod("()Landroid/nfc/Tag;")