from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkScan"]

class NetworkScan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/NetworkScan"
    ERROR_INTERRUPTED = JavaStaticField("I")
    ERROR_INVALID_SCAN = JavaStaticField("I")
    ERROR_INVALID_SCANID = JavaStaticField("I")
    ERROR_MODEM_ERROR = JavaStaticField("I")
    ERROR_MODEM_UNAVAILABLE = JavaStaticField("I")
    ERROR_RADIO_INTERFACE_ERROR = JavaStaticField("I")
    ERROR_UNSUPPORTED = JavaStaticField("I")
    SUCCESS = JavaStaticField("I")
    stopScan = JavaMethod("()V")