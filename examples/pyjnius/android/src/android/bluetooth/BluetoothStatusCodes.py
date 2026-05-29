from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothStatusCodes"]

class BluetoothStatusCodes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothStatusCodes"
    ERROR_BLUETOOTH_NOT_ALLOWED = JavaStaticField("I")
    ERROR_BLUETOOTH_NOT_ENABLED = JavaStaticField("I")
    ERROR_DEVICE_NOT_BONDED = JavaStaticField("I")
    ERROR_GATT_WRITE_NOT_ALLOWED = JavaStaticField("I")
    ERROR_GATT_WRITE_REQUEST_BUSY = JavaStaticField("I")
    ERROR_MISSING_BLUETOOTH_CONNECT_PERMISSION = JavaStaticField("I")
    ERROR_PROFILE_SERVICE_NOT_BOUND = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    FEATURE_NOT_CONFIGURED = JavaStaticField("I")
    FEATURE_NOT_SUPPORTED = JavaStaticField("I")
    FEATURE_SUPPORTED = JavaStaticField("I")
    SUCCESS = JavaStaticField("I")