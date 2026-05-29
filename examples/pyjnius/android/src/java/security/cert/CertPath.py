from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPath"]

class CertPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPath"
    getEncodings = JavaMethod("()Ljava/util/Iterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getCertificates = JavaMethod("()Ljava/util/List;")
    getType = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMultipleMethod([("(Ljava/lang/String;)[B", False, False), ("()[B", False, False)])