from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MifareUltralight"]

class MifareUltralight(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/MifareUltralight"
    PAGE_SIZE = JavaStaticField("I")
    TYPE_ULTRALIGHT = JavaStaticField("I")
    TYPE_ULTRALIGHT_C = JavaStaticField("I")
    TYPE_UNKNOWN = JavaStaticField("I")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/MifareUltralight;")
    getType = JavaMethod("()I")
    readPages = JavaMethod("(I)[B")
    writePage = JavaMethod("(I[B)V")
    transceive = JavaMethod("([B)[B")
    getMaxTransceiveLength = JavaMethod("()I")
    setTimeout = JavaMethod("(I)V")
    getTimeout = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")