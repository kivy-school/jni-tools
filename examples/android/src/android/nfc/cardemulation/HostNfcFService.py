from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HostNfcFService"]

class HostNfcFService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/cardemulation/HostNfcFService"
    __javaconstructor__ = [("()V", False)]
    DEACTIVATION_LINK_LOSS = JavaStaticField("I")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    sendResponsePacket = JavaMethod("([B)V")
    processNfcFPacket = JavaMethod("([BLandroid/os/Bundle;)[B")
    onDeactivated = JavaMethod("(I)V")