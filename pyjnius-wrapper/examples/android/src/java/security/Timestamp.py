from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Timestamp"]

class Timestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Timestamp"
    __javaconstructor__ = [("(Ljava/util/Date;Ljava/security/cert/CertPath;)V", False)]
    getTimestamp = JavaMethod("()Ljava/util/Date;")
    getSignerCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")