from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NdefFormatable"]

class NdefFormatable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/NdefFormatable"
    connect = JavaMethod("()V")
    isConnected = JavaMethod("()Z")
    get = JavaStaticMethod("(Landroid/nfc/Tag;)Landroid/nfc/tech/NdefFormatable;")
    format = JavaMethod("(Landroid/nfc/NdefMessage;)V")
    close = JavaMethod("()V")
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    formatReadOnly = JavaMethod("(Landroid/nfc/NdefMessage;)V")