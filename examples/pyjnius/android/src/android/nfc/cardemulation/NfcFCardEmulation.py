from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcFCardEmulation"]

class NfcFCardEmulation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/cardemulation/NfcFCardEmulation"
    enableService = JavaMethod("(Landroid/app/Activity;Landroid/content/ComponentName;)Z")
    getNfcid2ForService = JavaMethod("(Landroid/content/ComponentName;)Ljava/lang/String;")
    getSystemCodeForService = JavaMethod("(Landroid/content/ComponentName;)Ljava/lang/String;")
    registerSystemCodeForService = JavaMethod("(Landroid/content/ComponentName;Ljava/lang/String;)Z")
    setNfcid2ForService = JavaMethod("(Landroid/content/ComponentName;Ljava/lang/String;)Z")
    unregisterSystemCodeForService = JavaMethod("(Landroid/content/ComponentName;)Z")
    disableService = JavaMethod("(Landroid/app/Activity;)Z")
    getInstance = JavaStaticMethod("(Landroid/nfc/NfcAdapter;)Landroid/nfc/cardemulation/NfcFCardEmulation;")