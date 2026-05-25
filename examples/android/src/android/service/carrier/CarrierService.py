from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CarrierService"]

class CarrierService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/carrier/CarrierService"
    __javaconstructor__ = [("()V", False)]
    CARRIER_SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onLoadConfig = JavaMultipleMethod([("(Landroid/service/carrier/CarrierIdentifier;)Landroid/os/PersistableBundle;", False, False), ("(ILandroid/service/carrier/CarrierIdentifier;)Landroid/os/PersistableBundle;", False, False)])
    notifyCarrierNetworkChange = JavaMultipleMethod([("(Z)V", False, False), ("(IZ)V", False, False)])
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")