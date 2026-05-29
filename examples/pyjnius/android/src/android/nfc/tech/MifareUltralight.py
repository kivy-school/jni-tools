from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MifareUltralight"]

class MifareUltralight(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/MifareUltralight"
    PAGE_SIZE = JavaStaticField("I")
    TYPE_ULTRALIGHT = JavaStaticField("I")
    TYPE_ULTRALIGHT_C = JavaStaticField("I")
    TYPE_UNKNOWN = JavaStaticField("I")
    connect = JavaMethod("()V")
    readPages = JavaMethod("(I)[B")
    getTimeout = JavaMethod("()I")
    setTimeout = JavaMethod("(I)V")
    writePage = JavaMethod("(I[B)V")
    getMaxTransceiveLength = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    transceive = JavaMethod("([B)[B")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/MifareUltralight;")
    close = JavaMethod("()V")
    getType = JavaMethod("()I")
    getTag = JavaMethod("()Landroid/nfc/Tag;")