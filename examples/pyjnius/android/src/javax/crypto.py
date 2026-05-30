from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CipherInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherInputStream"
    __javaconstructor__ = [("(Ljava/io/InputStream;Ljavax/crypto/Cipher;)V", False)]
    read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False), ("([B)I", False, False)])
    close = JavaMethod("()V")
    skip = JavaMethod("(J)J")
    available = JavaMethod("()I")
    markSupported = JavaMethod("()Z")

class KeyGeneratorSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyGeneratorSpi"
    __javaconstructor__ = [("()V", False)]

class CipherSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherSpi"
    __javaconstructor__ = [("()V", False)]

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
    doFinal = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False), ("([BII[BI)I", False, False), ("([BII[B)I", False, False), ("([BII)[B", False, False), ("([B)[B", False, False), ("([BI)I", False, False), ("()[B", False, False)])
    getExemptionMechanism = JavaMethod("()Ljavax/crypto/ExemptionMechanism;")
    updateAAD = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)V", False, False), ("([BII)V", False, False), ("([B)V", False, False)])
    getBlockSize = JavaMethod("()I")
    getOutputSize = JavaMethod("(I)I")
    getIV = JavaMethod("()[B")
    getMaxAllowedKeyLength = JavaStaticMethod("(Ljava/lang/String;)I")
    getMaxAllowedParameterSpec = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/spec/AlgorithmParameterSpec;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    update = JavaMultipleMethod([("([BII[B)I", False, False), ("([B)[B", False, False), ("([BII[BI)I", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False), ("([BII)[B", False, False)])
    wrap = JavaMethod("(Ljava/security/Key;)[B")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/Cipher;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/Cipher;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/Cipher;", True, False)])
    init = JavaMultipleMethod([("(ILjava/security/Key;)V", False, False), ("(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/cert/Certificate;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/AlgorithmParameters;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/cert/Certificate;)V", False, False), ("(ILjava/security/Key;Ljava/security/AlgorithmParameters;)V", False, False), ("(ILjava/security/Key;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False)])
    getParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    unwrap = JavaMethod("([BLjava/lang/String;I)Ljava/security/Key;")

class SecretKeyFactorySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKeyFactorySpi"
    __javaconstructor__ = [("()V", False)]

class NoSuchPaddingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/NoSuchPaddingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class CipherOutputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherOutputStream"
    __javaconstructor__ = [("(Ljava/io/OutputStream;Ljavax/crypto/Cipher;)V", False)]
    flush = JavaMethod("()V")
    write = JavaMultipleMethod([("([BII)V", False, False), ("(I)V", False, False), ("([B)V", False, False)])
    close = JavaMethod("()V")

class SecretKeyFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKeyFactory"
    generateSecret = JavaMethod("(Ljava/security/spec/KeySpec;)Ljavax/crypto/SecretKey;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/SecretKeyFactory;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;", True, False)])
    getKeySpec = JavaMethod("(Ljavax/crypto/SecretKey;Ljava/lang/Class;)Ljava/security/spec/KeySpec;")
    translateKey = JavaMethod("(Ljavax/crypto/SecretKey;)Ljavax/crypto/SecretKey;")

class ExemptionMechanismSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanismSpi"
    __javaconstructor__ = [("()V", False)]

class SealedObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SealedObject"
    __javaconstructor__ = [("(Ljava/io/Serializable;Ljavax/crypto/Cipher;)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getObject = JavaMultipleMethod([("(Ljava/security/Key;Ljava/lang/String;)Ljava/lang/Object;", False, False), ("(Ljava/security/Key;)Ljava/lang/Object;", False, False), ("(Ljavax/crypto/Cipher;)Ljava/lang/Object;", False, False)])

class NullCipher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/NullCipher"
    __javaconstructor__ = [("()V", False)]
    ENCRYPT_MODE = JavaStaticField("I")
    DECRYPT_MODE = JavaStaticField("I")
    WRAP_MODE = JavaStaticField("I")
    UNWRAP_MODE = JavaStaticField("I")
    PUBLIC_KEY = JavaStaticField("I")
    PRIVATE_KEY = JavaStaticField("I")
    SECRET_KEY = JavaStaticField("I")

class SecretKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/SecretKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")

class KeyAgreementSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyAgreementSpi"
    __javaconstructor__ = [("()V", False)]

class ExemptionMechanismException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanismException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class KeyGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyGenerator"
    generateKey = JavaMethod("()Ljavax/crypto/SecretKey;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/KeyGenerator;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/KeyGenerator;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/KeyGenerator;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(I)V", False, False), ("(ILjava/security/SecureRandom;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/SecureRandom;)V", False, False)])

class BadPaddingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/BadPaddingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class MacSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/MacSpi"
    __javaconstructor__ = [("()V", False)]
    clone = JavaMethod("()Ljava/lang/Object;")

class KeyAgreement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/KeyAgreement"
    generateSecret = JavaMultipleMethod([("([BI)I", False, False), ("()[B", False, False), ("(Ljava/lang/String;)Ljavax/crypto/SecretKey;", False, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    doPhase = JavaMethod("(Ljava/security/Key;Z)Ljava/security/Key;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/KeyAgreement;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/KeyAgreement;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/KeyAgreement;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/Key;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(Ljava/security/Key;Ljava/security/SecureRandom;)V", False, False)])

class EncryptedPrivateKeyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/EncryptedPrivateKeyInfo"
    __javaconstructor__ = [("(Ljava/lang/String;[B)V", False), ("([B)V", False), ("(Ljava/security/AlgorithmParameters;[B)V", False)]
    getAlgName = JavaMethod("()Ljava/lang/String;")
    getAlgParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    getEncryptedData = JavaMethod("()[B")
    getEncoded = JavaMethod("()[B")
    getKeySpec = JavaMultipleMethod([("(Ljava/security/Key;Ljava/lang/String;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljava/security/Key;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljava/security/Key;Ljava/security/Provider;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False), ("(Ljavax/crypto/Cipher;)Ljava/security/spec/PKCS8EncodedKeySpec;", False, False)])

class IllegalBlockSizeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/IllegalBlockSizeException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class Mac(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/Mac"
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getMacLength = JavaMethod("()I")
    doFinal = JavaMultipleMethod([("([BI)V", False, False), ("([B)[B", False, False), ("()[B", False, False)])
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    reset = JavaMethod("()V")
    clone = JavaMethod("()Ljava/lang/Object;")
    update = JavaMultipleMethod([("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False), ("([B)V", False, False), ("(B)V", False, False)])
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljavax/crypto/Mac;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/Mac;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/Mac;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/Key;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False)])

class ExemptionMechanism(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ExemptionMechanism"
    genExemptionBlob = JavaMultipleMethod([("()[B", False, False), ("([B)I", False, False), ("([BI)I", False, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    isCryptoAllowed = JavaMethod("(Ljava/security/Key;)Z")
    getOutputSize = JavaMethod("(I)I")
    getName = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljavax/crypto/ExemptionMechanism;", True, False), ("(Ljava/lang/String;)Ljavax/crypto/ExemptionMechanism;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljavax/crypto/ExemptionMechanism;", True, False)])
    init = JavaMultipleMethod([("(Ljava/security/Key;Ljava/security/AlgorithmParameters;)V", False, False), ("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V", False, False), ("(Ljava/security/Key;)V", False, False)])

class ShortBufferException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ShortBufferException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class AEADBadTagException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/AEADBadTagException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]