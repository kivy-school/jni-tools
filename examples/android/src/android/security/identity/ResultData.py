from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResultData"]

class ResultData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/ResultData"
    STATUS_NOT_IN_REQUEST_MESSAGE = JavaStaticField("I")
    STATUS_NOT_REQUESTED = JavaStaticField("I")
    STATUS_NO_ACCESS_CONTROL_PROFILES = JavaStaticField("I")
    STATUS_NO_SUCH_ENTRY = JavaStaticField("I")
    STATUS_OK = JavaStaticField("I")
    STATUS_READER_AUTHENTICATION_FAILED = JavaStaticField("I")
    STATUS_USER_AUTHENTICATION_FAILED = JavaStaticField("I")
    getAuthenticatedData = JavaMethod("()[B")
    getMessageAuthenticationCode = JavaMethod("()[B")
    getStaticAuthenticationData = JavaMethod("()[B")
    getNamespaces = JavaMethod("()Ljava/util/Collection;")
    getEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
    getRetrievedEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
    getStatus = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)I")
    getEntry = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)[B")