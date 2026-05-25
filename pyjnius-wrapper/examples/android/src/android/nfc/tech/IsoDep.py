from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsoDep"]

class IsoDep(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/IsoDep"
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/IsoDep;")
    setTimeout = JavaMethod("(I)V")
    getTimeout = JavaMethod("()I")
    getHistoricalBytes = JavaMethod("()[B")
    getHiLayerResponse = JavaMethod("()[B")
    transceive = JavaMethod("([B)[B")
    getMaxTransceiveLength = JavaMethod("()I")
    isExtendedLengthApduSupported = JavaMethod("()Z")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")