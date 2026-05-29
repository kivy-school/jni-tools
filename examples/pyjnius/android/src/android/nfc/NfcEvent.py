from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcEvent"]

class NfcEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/NfcEvent"
    nfcAdapter = JavaField("Landroid/nfc/NfcAdapter;")
    peerLlcpMajorVersion = JavaField("I")
    peerLlcpMinorVersion = JavaField("I")