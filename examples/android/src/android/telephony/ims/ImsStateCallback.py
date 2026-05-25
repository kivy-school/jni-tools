from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsStateCallback"]

class ImsStateCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsStateCallback"
    __javaconstructor__ = [("()V", False)]
    REASON_IMS_SERVICE_DISCONNECTED = JavaStaticField("I")
    REASON_IMS_SERVICE_NOT_READY = JavaStaticField("I")
    REASON_NO_IMS_SERVICE_CONFIGURED = JavaStaticField("I")
    REASON_SUBSCRIPTION_INACTIVE = JavaStaticField("I")
    REASON_UNKNOWN_PERMANENT_ERROR = JavaStaticField("I")
    REASON_UNKNOWN_TEMPORARY_ERROR = JavaStaticField("I")
    onUnavailable = JavaMethod("(I)V")
    onAvailable = JavaMethod("()V")
    onError = JavaMethod("()V")