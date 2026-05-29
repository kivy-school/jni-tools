from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EncryptedPrivateKeyInfo"]

class EncryptedPrivateKeyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/EncryptedPrivateKeyInfo"
    __javaconstructor__ = [("([B)V", False), ("(Ljava/lang/String;[B)V", False), ("(Ljava/security/AlgorithmParameters;[B)V", False)]
    getAlgName = JavaMethod("()Ljava/lang/String;")
    getAlgParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    getEncryptedData = JavaMethod("()[B")
    getKeySpec = JavaMultipleMethod([("(Ljavax/crypto/Cipher;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljava/security/Key;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljava/security/Key;Ljava/lang/String;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljava/security/Key;Ljava/security/Provider;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False)])
    getEncoded = JavaMethod("()[B")