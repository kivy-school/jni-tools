from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertiseCallback"]

class AdvertiseCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertiseCallback"
    __javaconstructor__ = [("()V", False)]
    ADVERTISE_FAILED_ALREADY_STARTED = JavaStaticField("I")
    ADVERTISE_FAILED_DATA_TOO_LARGE = JavaStaticField("I")
    ADVERTISE_FAILED_FEATURE_UNSUPPORTED = JavaStaticField("I")
    ADVERTISE_FAILED_INTERNAL_ERROR = JavaStaticField("I")
    ADVERTISE_FAILED_TOO_MANY_ADVERTISERS = JavaStaticField("I")
    onStartSuccess = JavaMethod("(Landroid/bluetooth/le/AdvertiseSettings;)V")
    onStartFailure = JavaMethod("(I)V")