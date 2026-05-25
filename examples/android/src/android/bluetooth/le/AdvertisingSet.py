from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertisingSet"]

class AdvertisingSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertisingSet"
    enableAdvertising = JavaMethod("(ZII)V")
    setAdvertisingData = JavaMethod("(Landroid/bluetooth/le/AdvertiseData;)V")
    setScanResponseData = JavaMethod("(Landroid/bluetooth/le/AdvertiseData;)V")
    setAdvertisingParameters = JavaMethod("(Landroid/bluetooth/le/AdvertisingSetParameters;)V")
    setPeriodicAdvertisingParameters = JavaMethod("(Landroid/bluetooth/le/PeriodicAdvertisingParameters;)V")
    setPeriodicAdvertisingData = JavaMethod("(Landroid/bluetooth/le/AdvertiseData;)V")
    setPeriodicAdvertisingEnabled = JavaMethod("(Z)V")