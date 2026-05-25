from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Certificate"]

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/Certificate"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;)V", False, False), ("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")