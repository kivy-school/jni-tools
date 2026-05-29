from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcBarcode"]

class NfcBarcode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcBarcode"
    TYPE_KOVIO = JavaStaticField("I")
    TYPE_UNKNOWN = JavaStaticField("I")
    connect = JavaMethod("()V")
    getBarcode = JavaMethod("()[B")
    isConnected = JavaMethod("()Z")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcBarcode;")
    close = JavaMethod("()V")
    getType = JavaMethod("()I")
    getTag = JavaMethod("()Landroid/nfc/Tag;")