from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertisingSetCallback"]

class AdvertisingSetCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertisingSetCallback"
    __javaconstructor__ = [("()V", False)]
    ADVERTISE_FAILED_ALREADY_STARTED = JavaStaticField("I")
    ADVERTISE_FAILED_DATA_TOO_LARGE = JavaStaticField("I")
    ADVERTISE_FAILED_FEATURE_UNSUPPORTED = JavaStaticField("I")
    ADVERTISE_FAILED_INTERNAL_ERROR = JavaStaticField("I")
    ADVERTISE_FAILED_TOO_MANY_ADVERTISERS = JavaStaticField("I")
    ADVERTISE_SUCCESS = JavaStaticField("I")
    onAdvertisingSetStarted = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;II)V")
    onAdvertisingSetStopped = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;)V")
    onAdvertisingEnabled = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;ZI)V")
    onAdvertisingDataSet = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;I)V")
    onScanResponseDataSet = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;I)V")
    onAdvertisingParametersUpdated = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;II)V")
    onPeriodicAdvertisingParametersUpdated = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;I)V")
    onPeriodicAdvertisingDataSet = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;I)V")
    onPeriodicAdvertisingEnabled = JavaMethod("(Landroid/bluetooth/le/AdvertisingSet;ZI)V")