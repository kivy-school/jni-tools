from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPathValidatorException"]

class CertPathValidatorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPathValidatorException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;Ljava/security/cert/CertPath;I)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;Ljava/security/cert/CertPath;ILjava/security/cert/CertPathValidatorException$Reason;)V", False)]
    getCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    getIndex = JavaMethod("()I")
    getReason = JavaMethod("()Ljava/security/cert/CertPathValidatorException$Reason;")

    class BasicReason(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/cert/CertPathValidatorException/BasicReason"
        values = JavaStaticMethod("()[Ljava/security/cert/CertPathValidatorException$BasicReason;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/cert/CertPathValidatorException$BasicReason;")
        UNSPECIFIED = JavaStaticField("Ljava/security/cert/CertPathValidatorException/BasicReason;")
        EXPIRED = JavaStaticField("Ljava/security/cert/CertPathValidatorException/BasicReason;")
        NOT_YET_VALID = JavaStaticField("Ljava/security/cert/CertPathValidatorException/BasicReason;")
        REVOKED = JavaStaticField("Ljava/security/cert/CertPathValidatorException/BasicReason;")
        UNDETERMINED_REVOCATION_STATUS = JavaStaticField("Ljava/security/cert/CertPathValidatorException/BasicReason;")
        INVALID_SIGNATURE = JavaStaticField("Ljava/security/cert/CertPathValidatorException/BasicReason;")
        ALGORITHM_CONSTRAINED = JavaStaticField("Ljava/security/cert/CertPathValidatorException/BasicReason;")

    class Reason(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/cert/CertPathValidatorException/Reason"