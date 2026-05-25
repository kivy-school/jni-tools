from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompanionDeviceService"]

class CompanionDeviceService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/CompanionDeviceService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onDeviceAppeared = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Landroid/companion/AssociationInfo;)V", False, False)])
    onDeviceDisappeared = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Landroid/companion/AssociationInfo;)V", False, False)])
    attachSystemDataTransport = JavaMethod("(ILjava/io/InputStream;Ljava/io/OutputStream;)V")
    detachSystemDataTransport = JavaMethod("(I)V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")