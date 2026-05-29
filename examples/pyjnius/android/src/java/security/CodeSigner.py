from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CodeSigner"]

class CodeSigner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/CodeSigner"
    __javaconstructor__ = [("(Ljava/security/cert/CertPath;Ljava/security/Timestamp;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSignerCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    getTimestamp = JavaMethod("()Ljava/security/Timestamp;")