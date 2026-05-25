from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertPath"]

class CertPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertPath"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getType = JavaMethod("()Ljava/lang/String;")
    getEncodings = JavaMethod("()Ljava/util/Iterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMultipleMethod([("()[B", False, False), ("(Ljava/lang/String;)[B", False, False)])
    getCertificates = JavaMethod("()Ljava/util/List;")
    writeReplace = JavaMethod("()Ljava/lang/Object;")

    class CertPathRep(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/cert/CertPath/CertPathRep"
        __javaconstructor__ = [("(Ljava/lang/String;[B)V", False)]
        readResolve = JavaMethod("()Ljava/lang/Object;")