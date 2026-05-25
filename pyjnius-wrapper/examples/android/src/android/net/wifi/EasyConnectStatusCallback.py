from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EasyConnectStatusCallback"]

class EasyConnectStatusCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/EasyConnectStatusCallback"
    EASY_CONNECT_EVENT_FAILURE_AUTHENTICATION = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_BUSY = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_CANNOT_FIND_NETWORK = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_CONFIGURATION = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_ENROLLEE_AUTHENTICATION = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_ENROLLEE_FAILED_TO_SCAN_NETWORK_CHANNEL = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_ENROLLEE_REJECTED_CONFIGURATION = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_GENERIC = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_INVALID_NETWORK = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_INVALID_URI = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_NOT_COMPATIBLE = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_NOT_SUPPORTED = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_TIMEOUT = JavaStaticField("I")
    EASY_CONNECT_EVENT_FAILURE_URI_GENERATION = JavaStaticField("I")