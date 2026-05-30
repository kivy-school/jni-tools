from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DESKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DESKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BI)V", False)]
    DES_KEY_LEN = JavaStaticField("I")
    isParityAdjusted = JavaStaticMethod("([BI)Z")
    isWeak = JavaStaticMethod("([BI)Z")
    getKey = JavaMethod("()[B")

class SecretKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/SecretKeySpec"
    __javaconstructor__ = [("([BLjava/lang/String;)V", False), ("([BIILjava/lang/String;)V", False)]
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getFormat = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")

class DHParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DHParameterSpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;I)V", False)]
    getL = JavaMethod("()I")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")

class GCMParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/GCMParameterSpec"
    __javaconstructor__ = [("(I[B)V", False), ("(I[BII)V", False)]
    getTLen = JavaMethod("()I")
    getIV = JavaMethod("()[B")

class PBEKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/PBEKeySpec"
    __javaconstructor__ = [("([C)V", False), ("([C[BII)V", False), ("([C[BI)V", False)]
    getIterationCount = JavaMethod("()I")
    getSalt = JavaMethod("()[B")
    getKeyLength = JavaMethod("()I")
    getPassword = JavaMethod("()[C")
    clearPassword = JavaMethod("()V")

class DHPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DHPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getX = JavaMethod("()Ljava/math/BigInteger;")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")

class RC5ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/RC5ParameterSpec"
    __javaconstructor__ = [("(III)V", False), ("(III[BI)V", False), ("(III[B)V", False)]
    getRounds = JavaMethod("()I")
    getWordSize = JavaMethod("()I")
    getIV = JavaMethod("()[B")
    getVersion = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class DESedeKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DESedeKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BI)V", False)]
    DES_EDE_KEY_LEN = JavaStaticField("I")
    isParityAdjusted = JavaStaticMethod("([BI)Z")
    getKey = JavaMethod("()[B")

class PBEParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/PBEParameterSpec"
    __javaconstructor__ = [("([BILjava/security/spec/AlgorithmParameterSpec;)V", False), ("([BI)V", False)]
    getIterationCount = JavaMethod("()I")
    getSalt = JavaMethod("()[B")
    getParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")

class IvParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/IvParameterSpec"
    __javaconstructor__ = [("([BII)V", False), ("([B)V", False)]
    getIV = JavaMethod("()[B")

class OAEPParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/OAEPParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;Ljavax/crypto/spec/PSource;)V", False)]
    DEFAULT = JavaStaticField("Ljavax/crypto/spec/OAEPParameterSpec;")
    getPSource = JavaMethod("()Ljavax/crypto/spec/PSource;")
    getDigestAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFParameters = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")

class ChaCha20ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/ChaCha20ParameterSpec"
    __javaconstructor__ = [("([BI)V", False)]
    getNonce = JavaMethod("()[B")
    getCounter = JavaMethod("()I")

class DHGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DHGenParameterSpec"
    __javaconstructor__ = [("(II)V", False)]
    getPrimeSize = JavaMethod("()I")
    getExponentSize = JavaMethod("()I")

class DHPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/DHPublicKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getY = JavaMethod("()Ljava/math/BigInteger;")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")

class RC2ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/RC2ParameterSpec"
    __javaconstructor__ = [("(I)V", False), ("(I[BI)V", False), ("(I[B)V", False)]
    getEffectiveKeyBits = JavaMethod("()I")
    getIV = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class PSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/spec/PSource"
    getAlgorithm = JavaMethod("()Ljava/lang/String;")

    class PSpecified(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/crypto/spec/PSource$PSpecified"
        __javaconstructor__ = [("([B)V", False)]
        DEFAULT = JavaStaticField("Ljavax/crypto/spec/PSource$PSpecified;")
        getValue = JavaMethod("()[B")