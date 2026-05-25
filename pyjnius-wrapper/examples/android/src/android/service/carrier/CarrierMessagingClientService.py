from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CarrierMessagingClientService"]

class CarrierMessagingClientService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/carrier/CarrierMessagingClientService"
    __javaconstructor__ = [("()V", False)]
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")