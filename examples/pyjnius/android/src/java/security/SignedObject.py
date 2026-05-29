from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignedObject"]

class SignedObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SignedObject"
    __javaconstructor__ = [("(Ljava/io/Serializable;Ljava/security/PrivateKey;Ljava/security/Signature;)V", False)]
    getObject = JavaMethod("()Ljava/lang/Object;")
    getSignature = JavaMethod("()[B")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    verify = JavaMethod("(Ljava/security/PublicKey;Ljava/security/Signature;)Z")