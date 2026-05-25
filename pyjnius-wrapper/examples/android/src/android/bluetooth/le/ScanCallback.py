from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScanCallback"]

class ScanCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/ScanCallback"
    __javaconstructor__ = [("()V", False)]
    SCAN_FAILED_ALREADY_STARTED = JavaStaticField("I")
    SCAN_FAILED_APPLICATION_REGISTRATION_FAILED = JavaStaticField("I")
    SCAN_FAILED_FEATURE_UNSUPPORTED = JavaStaticField("I")
    SCAN_FAILED_INTERNAL_ERROR = JavaStaticField("I")
    SCAN_FAILED_OUT_OF_HARDWARE_RESOURCES = JavaStaticField("I")
    SCAN_FAILED_SCANNING_TOO_FREQUENTLY = JavaStaticField("I")
    onScanResult = JavaMethod("(ILandroid/bluetooth/le/ScanResult;)V")
    onBatchScanResults = JavaMethod("(Ljava/util/List;)V")
    onScanFailed = JavaMethod("(I)V")