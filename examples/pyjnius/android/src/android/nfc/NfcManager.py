from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcManager"]

class NfcManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/NfcManager"
    getDefaultAdapter = JavaMethod("()Landroid/nfc/NfcAdapter;")