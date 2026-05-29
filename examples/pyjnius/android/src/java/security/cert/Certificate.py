from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Certificate"]

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/Certificate"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False), ("(Ljava/security/PublicKey;Ljava/security/Provider;)V", False, False)])
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")