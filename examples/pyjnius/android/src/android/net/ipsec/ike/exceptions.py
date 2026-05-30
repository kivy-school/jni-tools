from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IkeNonProtocolException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeNonProtocolException"

class InvalidSelectorsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/InvalidSelectorsException"
    __javaconstructor__ = [("(I[B)V", False)]
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
    getIpSecPacketInfo = JavaMethod("()[B")
    getIpSecSpi = JavaMethod("()I")

class InvalidMajorVersionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/InvalidMajorVersionException"
    __javaconstructor__ = [("(B)V", False)]
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
    getMajorVersion = JavaMethod("()B")

class IkeTimeoutException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeTimeoutException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

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

class IkeInternalException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeInternalException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]

class IkeNetworkLostException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeNetworkLostException"
    __javaconstructor__ = [("(Landroid/net/Network;)V", False)]
    getNetwork = JavaMethod("()Landroid/net/Network;")

class InvalidKeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/InvalidKeException"
    __javaconstructor__ = [("(I)V", False)]
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
    getDhGroup = JavaMethod("()I")

class IkeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeException"

class IkeIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeIOException"
    __javaconstructor__ = [("(Ljava/io/IOException;)V", False)]
    getCause = JavaMultipleMethod([("()Ljava/lang/Throwable;", False, False), ("()Ljava/io/IOException;", False, False)])
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")