from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Cipher"]

class Cipher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/Cipher"
    __javaconstructor__ = [("(Ljavax/crypto/CipherSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    DECRYPT_MODE = JavaStaticField("I")
    ENCRYPT_MODE = JavaStaticField("I")
    PRIVATE_KEY = JavaStaticField("I")
    PUBLIC_KEY = JavaStaticField("I")
    SECRET_KEY = JavaStaticField("I")
    UNWRAP_MODE = JavaStaticField("I")
    WRAP_MODE = JavaStaticField("I")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/Cipher;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/Cipher;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/Cipher;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getBlockSize = JavaMethod("()I")
    getOutputSize = JavaMethod("(I)I")
    getIV = JavaMethod("()[B")
    getParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    getExemptionMechanism = JavaMethod("()Ljavax/crypto/ExemptionMechanism;")
    init = JavaMultipleMethod([("(ILjava/security/Key;)V", False, False), ("(ILjava/security/Key;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/AlgorithmParameters;)V", False, False), ("(ILjava/security/Key;Ljava/security/AlgorithmParameters;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/cert/Certificate;)V", False, False), ("(ILjava/security/cert/Certificate;Ljava/security/SecureRandom;)V", False, False)])
    update = JavaMultipleMethod([("([B)[B", False, False), ("([BII)[B", False, False), ("([BII[B)I", False, False), ("([BII[BI)I", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False)])
    doFinal = JavaMultipleMethod([("()[B", False, False), ("([BI)I", False, False), ("([B)[B", False, False), ("([BII)[B", False, False), ("([BII[B)I", False, False), ("([BII[BI)I", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False)])
    wrap = JavaMethod("(Ljava/security/Key;)[B")
    unwrap = JavaMethod("([BLjava/lang/String;I)Ljava/security/Key;")
    getMaxAllowedKeyLength = JavaStaticMethod("(Ljava/lang/String;)I")
    getMaxAllowedParameterSpec = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/spec/AlgorithmParameterSpec;")
    updateAAD = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])