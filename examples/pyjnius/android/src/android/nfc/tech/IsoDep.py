from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsoDep"]

class IsoDep(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/IsoDep"
    connect = JavaMethod("()V")
    getTimeout = JavaMethod("()I")
    setTimeout = JavaMethod("(I)V")
    getHistoricalBytes = JavaMethod("()[B")
    getMaxTransceiveLength = JavaMethod("()I")
    isConnected = JavaMethod("()Z")
    transceive = JavaMethod("([B)[B")
    getHiLayerResponse = JavaMethod("()[B")
    isExtendedLengthApduSupported = JavaMethod("()Z")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/IsoDep;")
    close = JavaMethod("()V")
    getTag = JavaMethod("()Landroid/nfc/Tag;")