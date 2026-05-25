from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CRLReason"]

class CRLReason(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CRLReason"
    values = JavaStaticMethod("()[Ljava/security/cert/CRLReason;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/cert/CRLReason;")
    UNSPECIFIED = JavaStaticField("Ljava/security/cert/CRLReason;")
    KEY_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")
    CA_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")
    AFFILIATION_CHANGED = JavaStaticField("Ljava/security/cert/CRLReason;")
    SUPERSEDED = JavaStaticField("Ljava/security/cert/CRLReason;")
    CESSATION_OF_OPERATION = JavaStaticField("Ljava/security/cert/CRLReason;")
    CERTIFICATE_HOLD = JavaStaticField("Ljava/security/cert/CRLReason;")
    UNUSED = JavaStaticField("Ljava/security/cert/CRLReason;")
    REMOVE_FROM_CRL = JavaStaticField("Ljava/security/cert/CRLReason;")
    PRIVILEGE_WITHDRAWN = JavaStaticField("Ljava/security/cert/CRLReason;")
    AA_COMPROMISE = JavaStaticField("Ljava/security/cert/CRLReason;")