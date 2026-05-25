from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OffHostApduService"]

class OffHostApduService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/cardemulation/OffHostApduService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")