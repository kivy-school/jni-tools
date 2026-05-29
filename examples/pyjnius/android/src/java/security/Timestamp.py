from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Timestamp"]

class Timestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Timestamp"
    __javaconstructor__ = [("(Ljava/util/Date;Ljava/security/cert/CertPath;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSignerCertPath = JavaMethod("()Ljava/security/cert/CertPath;")
    getTimestamp = JavaMethod("()Ljava/util/Date;")