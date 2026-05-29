from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertisingSet"]

class AdvertisingSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertisingSet"
    setAdvertisingData = JavaMethod("(Landroid/bluetooth/le/AdvertiseData;)V")
    enableAdvertising = JavaMethod("(ZII)V")
    setAdvertisingParameters = JavaMethod("(Landroid/bluetooth/le/AdvertisingSetParameters;)V")
    setPeriodicAdvertisingData = JavaMethod("(Landroid/bluetooth/le/AdvertiseData;)V")
    setPeriodicAdvertisingEnabled = JavaMethod("(Z)V")
    setPeriodicAdvertisingParameters = JavaMethod("(Landroid/bluetooth/le/PeriodicAdvertisingParameters;)V")
    setScanResponseData = JavaMethod("(Landroid/bluetooth/le/AdvertiseData;)V")