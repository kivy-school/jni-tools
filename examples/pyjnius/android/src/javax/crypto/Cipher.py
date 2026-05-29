from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Cipher"]

class Cipher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/Cipher"
    ENCRYPT_MODE = JavaStaticField("I")
    DECRYPT_MODE = JavaStaticField("I")
    WRAP_MODE = JavaStaticField("I")
    UNWRAP_MODE = JavaStaticField("I")
    PUBLIC_KEY = JavaStaticField("I")
    PRIVATE_KEY = JavaStaticField("I")
    SECRET_KEY = JavaStaticField("I")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    doFinal = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False), ("([BII[BI)I", False, False), ("([BII[B)I", False, False), ("([BII)[B", False, False), ("([B)[B", False, False), ("()[B", False, False), ("([BI)I", False, False)])
    getExemptionMechanism = JavaMethod("()Ljavax/crypto/ExemptionMechanism;")
    updateAAD = JavaMultipleMethod([("([B)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False), ("([BII)V", False, False)])
    getBlockSize = JavaMethod("()I")
    getOutputSize = JavaMethod("(I)I")
    getIV = JavaMethod("()[B")
    getMaxAllowedKeyLength = JavaStaticMethod("(Ljava/lang/String;)I")
    getMaxAllowedParameterSpec = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/spec/AlgorithmParameterSpec;")
    toString = JavaMethod("()Ljava/lang/String;")
    update = JavaMultipleMethod([("([BII[B)I", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False), ("([BII[BI)I", False, False), ("([B)[B", False, False), ("([BII)[B", False, False)])
    wrap = JavaMethod("(Ljava/security/Key;)[B")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/Cipher;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/Cipher;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/Cipher;", True, False)])
    init = JavaMultipleMethod([("(ILjava/security/Key;)V", False, False), ("(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/AlgorithmParameters;)V", False, False), ("(ILjava/security/Key;Ljava/security/AlgorithmParameters;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/cert/Certificate;)V", False, False), ("(ILjava/security/cert/Certificate;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/SecureRandom;)V", False, False)])
    getParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    unwrap = JavaMethod("([BLjava/lang/String;I)Ljava/security/Key;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")