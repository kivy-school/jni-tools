from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SealedObject"]

class SealedObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SealedObject"
    __javaconstructor__ = [("(Ljava/io/Serializable;Ljavax/crypto/Cipher;)V", False)]
    getObject = JavaMultipleMethod([("(Ljava/security/Key;)Ljava/lang/Object;", False, False), ("(Ljavax/crypto/Cipher;)Ljava/lang/Object;", False, False), ("(Ljava/security/Key;Ljava/lang/String;)Ljava/lang/Object;", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")