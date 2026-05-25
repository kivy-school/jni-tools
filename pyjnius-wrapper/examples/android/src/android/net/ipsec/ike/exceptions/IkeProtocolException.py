from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeProtocolException"]

class IkeProtocolException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeProtocolException"
    ERROR_TYPE_AUTHENTICATION_FAILED = JavaStaticField("I")
    ERROR_TYPE_CHILD_SA_NOT_FOUND = JavaStaticField("I")
    ERROR_TYPE_FAILED_CP_REQUIRED = JavaStaticField("I")
    ERROR_TYPE_INTERNAL_ADDRESS_FAILURE = JavaStaticField("I")
    ERROR_TYPE_INVALID_IKE_SPI = JavaStaticField("I")
    ERROR_TYPE_INVALID_KE_PAYLOAD = JavaStaticField("I")
    ERROR_TYPE_INVALID_MAJOR_VERSION = JavaStaticField("I")
    ERROR_TYPE_INVALID_MESSAGE_ID = JavaStaticField("I")
    ERROR_TYPE_INVALID_SELECTORS = JavaStaticField("I")
    ERROR_TYPE_INVALID_SYNTAX = JavaStaticField("I")
    ERROR_TYPE_NO_ADDITIONAL_SAS = JavaStaticField("I")
    ERROR_TYPE_NO_PROPOSAL_CHOSEN = JavaStaticField("I")
    ERROR_TYPE_SINGLE_PAIR_REQUIRED = JavaStaticField("I")
    ERROR_TYPE_TEMPORARY_FAILURE = JavaStaticField("I")
    ERROR_TYPE_TS_UNACCEPTABLE = JavaStaticField("I")
    ERROR_TYPE_UNSUPPORTED_CRITICAL_PAYLOAD = JavaStaticField("I")
    getErrorType = JavaMethod("()I")