from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ndef"]

class Ndef(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/Ndef"
    MIFARE_CLASSIC = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_1 = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_2 = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_3 = JavaStaticField("Ljava/lang/String;")
    NFC_FORUM_TYPE_4 = JavaStaticField("Ljava/lang/String;")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/Ndef;")
    getCachedNdefMessage = JavaMethod("()Landroid/nfc/NdefMessage;")
    getType = JavaMethod("()Ljava/lang/String;")
    getMaxSize = JavaMethod("()I")
    isWritable = JavaMethod("()Z")
    getNdefMessage = JavaMethod("()Landroid/nfc/NdefMessage;")
    writeNdefMessage = JavaMethod("(Landroid/nfc/NdefMessage;)V")
    canMakeReadOnly = JavaMethod("()Z")
    makeReadOnly = JavaMethod("()Z")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")