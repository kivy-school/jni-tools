from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXReason"]

class PKIXReason(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXReason"
    values = JavaStaticMethod("()[Ljava/security/cert/PKIXReason;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/cert/PKIXReason;")
    NAME_CHAINING = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_KEY_USAGE = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_POLICY = JavaStaticField("Ljava/security/cert/PKIXReason;")
    NO_TRUST_ANCHOR = JavaStaticField("Ljava/security/cert/PKIXReason;")
    UNRECOGNIZED_CRIT_EXT = JavaStaticField("Ljava/security/cert/PKIXReason;")
    NOT_CA_CERT = JavaStaticField("Ljava/security/cert/PKIXReason;")
    PATH_TOO_LONG = JavaStaticField("Ljava/security/cert/PKIXReason;")
    INVALID_NAME = JavaStaticField("Ljava/security/cert/PKIXReason;")