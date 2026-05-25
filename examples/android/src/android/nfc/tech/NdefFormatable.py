from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NdefFormatable"]

class NdefFormatable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NdefFormatable"
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NdefFormatable;")
    format = JavaMethod("(Landroid/nfc/NdefMessage;)V")
    formatReadOnly = JavaMethod("(Landroid/nfc/NdefMessage;)V")
    isConnected = JavaMethod("()Z")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    close = JavaMethod("()V")
    connect = JavaMethod("()V")