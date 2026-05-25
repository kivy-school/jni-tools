from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HostApduService"]

class HostApduService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/cardemulation/HostApduService"
    __javaconstructor__ = [("()V", False)]
    DEACTIVATION_DESELECTED = JavaStaticField("I")
    DEACTIVATION_LINK_LOSS = JavaStaticField("I")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    sendResponseApdu = JavaMethod("([B)V")
    notifyUnhandled = JavaMethod("()V")
    processPollingFrames = JavaMethod("(Ljava/util/List;)V")
    processCommandApdu = JavaMethod("([BLandroid/os/Bundle;)[B")
    onDeactivated = JavaMethod("(I)V")