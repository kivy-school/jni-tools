from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkException"]

class NetworkException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/NetworkException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]
    ERROR_ADDRESS_UNREACHABLE = JavaStaticField("I")
    ERROR_CONNECTION_CLOSED = JavaStaticField("I")
    ERROR_CONNECTION_REFUSED = JavaStaticField("I")
    ERROR_CONNECTION_RESET = JavaStaticField("I")
    ERROR_CONNECTION_TIMED_OUT = JavaStaticField("I")
    ERROR_HOSTNAME_NOT_RESOLVED = JavaStaticField("I")
    ERROR_INTERNET_DISCONNECTED = JavaStaticField("I")
    ERROR_NETWORK_CHANGED = JavaStaticField("I")
    ERROR_OTHER = JavaStaticField("I")
    ERROR_QUIC_PROTOCOL_FAILED = JavaStaticField("I")
    ERROR_TIMED_OUT = JavaStaticField("I")
    getErrorCode = JavaMethod("()I")
    isImmediatelyRetryable = JavaMethod("()Z")