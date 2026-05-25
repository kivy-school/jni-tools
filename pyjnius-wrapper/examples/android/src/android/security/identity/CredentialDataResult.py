from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialDataResult"]

class CredentialDataResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/CredentialDataResult"
    getDeviceNameSpaces = JavaMethod("()[B")
    getDeviceMac = JavaMethod("()[B")
    getDeviceSignature = JavaMethod("()[B")
    getStaticAuthenticationData = JavaMethod("()[B")
    getDeviceSignedEntries = JavaMethod("()Landroid/security/identity/CredentialDataResult$Entries;")
    getIssuerSignedEntries = JavaMethod("()Landroid/security/identity/CredentialDataResult$Entries;")

    class Entries(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/CredentialDataResult/Entries"
        STATUS_NOT_IN_REQUEST_MESSAGE = JavaStaticField("I")
        STATUS_NOT_REQUESTED = JavaStaticField("I")
        STATUS_NO_ACCESS_CONTROL_PROFILES = JavaStaticField("I")
        STATUS_NO_SUCH_ENTRY = JavaStaticField("I")
        STATUS_OK = JavaStaticField("I")
        STATUS_READER_AUTHENTICATION_FAILED = JavaStaticField("I")
        STATUS_USER_AUTHENTICATION_FAILED = JavaStaticField("I")
        getNamespaces = JavaMethod("()Ljava/util/Collection;")
        getEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
        getRetrievedEntryNames = JavaMethod("(Ljava/lang/String;)Ljava/util/Collection;")
        getStatus = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)I")
        getEntry = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)[B")