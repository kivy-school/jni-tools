from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RSAPrivateCrtKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPrivateCrtKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeQ = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentQ = JavaMethod("()Ljava/math/BigInteger;")
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")

class ECKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECKey"
    getParams = JavaMethod("()Ljava/security/spec/ECParameterSpec;")

class DSAPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getY = JavaMethod("()Ljava/math/BigInteger;")

class ECPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getW = JavaMethod("()Ljava/security/spec/ECPoint;")

class XECKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECKey"
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")

class EdECPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getPoint = JavaMethod("()Ljava/security/spec/EdECPoint;")

class XECPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getU = JavaMethod("()Ljava/math/BigInteger;")

class DSAPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getX = JavaMethod("()Ljava/math/BigInteger;")

class DSAParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAParams"
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getQ = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")

class XECPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/XECPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getScalar = JavaMethod("()Ljava/util/Optional;")

class RSAPublicKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPublicKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")

class RSAMultiPrimePrivateCrtKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAMultiPrimePrivateCrtKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeQ = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentQ = JavaMethod("()Ljava/math/BigInteger;")
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")
    getOtherPrimeInfo = JavaMethod("()[Ljava/security/spec/RSAOtherPrimeInfo;")

class DSAKeyPairGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAKeyPairGenerator"
    initialize = JavaMultipleMethod([("(Ljava/security/interfaces/DSAParams;Ljava/security/SecureRandom;)V", False, False), ("(IZLjava/security/SecureRandom;)V", False, False)])

class DSAKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/DSAKey"
    getParams = JavaMethod("()Ljava/security/interfaces/DSAParams;")

class EdECKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECKey"
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")

class RSAPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getPrivateExponent = JavaMethod("()Ljava/math/BigInteger;")

class RSAKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/RSAKey"
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getModulus = JavaMethod("()Ljava/math/BigInteger;")

class EdECPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/EdECPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getBytes = JavaMethod("()Ljava/util/Optional;")

class ECPrivateKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/interfaces/ECPrivateKey"
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    serialVersionUID = JavaStaticField("J")
    getS = JavaMethod("()Ljava/math/BigInteger;")