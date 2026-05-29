from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EncryptedPrivateKeyInfo"]

class EncryptedPrivateKeyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/EncryptedPrivateKeyInfo"
    __javaconstructor__ = [("([B)V", False), ("(Ljava/lang/String;[B)V", False), ("(Ljava/security/AlgorithmParameters;[B)V", False)]
    encrypt = JavaMultipleMethod([("(Ljava/security/DEREncodable;[C)Ljavax/crypto/EncryptedPrivateKeyInfo;", True, False), ("(Ljava/security/DEREncodable;[CLjava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/Provider;)Ljavax/crypto/EncryptedPrivateKeyInfo;", True, False), ("(Ljava/security/DEREncodable;Ljava/security/Key;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/Provider;Ljava/security/SecureRandom;)Ljavax/crypto/EncryptedPrivateKeyInfo;", True, False)])
    getKeyPair = JavaMultipleMethod([("([C)Ljava/security/KeyPair;", False, False), ("(Ljava/security/Key;Ljava/security/Provider;)Ljava/security/KeyPair;", False, False)])
    getKey = JavaMultipleMethod([("(Ljava/security/Key;Ljava/security/Provider;)Ljava/security/PrivateKey;", False, False), ("([C)Ljava/security/PrivateKey;", False, False)])
    getEncoded = JavaMethod("()[B")
    getAlgName = JavaMethod("()Ljava/lang/String;")
    getAlgParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    getEncryptedData = JavaMethod("()[B")
    getKeySpec = JavaMultipleMethod([("(Ljava/security/Key;Ljava/lang/String;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljavax/crypto/Cipher;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljava/security/Key;Ljava/security/Provider;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljava/security/Key;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False)])