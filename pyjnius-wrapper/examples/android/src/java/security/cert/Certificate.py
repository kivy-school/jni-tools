from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Certificate"]

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/Certificate"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getType = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False), ("(Ljava/security/PublicKey;Ljava/security/Provider;)V", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")
    writeReplace = JavaMethod("()Ljava/lang/Object;")

    class CertificateRep(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/cert/Certificate/CertificateRep"
        __javaconstructor__ = [("(Ljava/lang/String;[B)V", False)]
        readResolve = JavaMethod("()Ljava/lang/Object;")