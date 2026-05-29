from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Certificate"]

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/Certificate"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False), ("(Ljava/security/PublicKey;)V", False, False)])
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")