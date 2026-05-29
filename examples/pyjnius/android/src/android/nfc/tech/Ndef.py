from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ndef"]

class Ndef(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/Ndef"
    MIFARE_CLASSIC = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_1 = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_2 = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_3 = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_4 = JavaStaticField("Ljava/lang/String;")
    connect = JavaMethod("()V")
    canMakeReadOnly = JavaMethod("()Z")
    getCachedNdefMessage = JavaMethod("()Landroid/nfc/NdefMessage;")
    getNdefMessage = JavaMethod("()Landroid/nfc/NdefMessage;")
    makeReadOnly = JavaMethod("()Z")
    writeNdefMessage = JavaMethod("(Landroid/nfc/NdefMessage;)V")
    isConnected = JavaMethod("()Z")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/Ndef;")
    close = JavaMethod("()V")
    getType = JavaMethod("()Ljava/lang/String;")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    getMaxSize = JavaMethod("()I")
    isWritable = JavaMethod("()Z")