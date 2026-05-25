from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcBarcode"]

class NfcBarcode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NfcBarcode"
    TYPE_KOVIO = JavaStaticField("I")
    TYPE_UNKNOWN = JavaStaticField("I")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NfcBarcode;")
    getType = JavaMethod("()I")
    getBarcode = JavaMethod("()[B")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")