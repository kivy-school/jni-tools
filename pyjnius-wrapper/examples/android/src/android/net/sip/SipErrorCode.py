from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SipErrorCode"]

class SipErrorCode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/sip/SipErrorCode"
    CLIENT_ERROR = JavaStaticField("I")
    CROSS_DOMAIN_AUTHENTICATION = JavaStaticField("I")
    DATA_CONNECTION_LOST = JavaStaticField("I")
    INVALID_CREDENTIALS = JavaStaticField("I")
    INVALID_REMOTE_URI = JavaStaticField("I")
    IN_PROGRESS = JavaStaticField("I")
    NO_ERROR = JavaStaticField("I")
    PEER_NOT_REACHABLE = JavaStaticField("I")
    SERVER_ERROR = JavaStaticField("I")
    SERVER_UNREACHABLE = JavaStaticField("I")
    SOCKET_ERROR = JavaStaticField("I")
    TIME_OUT = JavaStaticField("I")
    TRANSACTION_TERMINTED = JavaStaticField("I")
    toString = JavaStaticMethod("(I)Ljava/lang/String;")