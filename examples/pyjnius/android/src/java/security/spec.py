from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DSAParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/DSAParameterSpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getQ = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")

class RSAKeyGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAKeyGenParameterSpec"
    __javaconstructor__ = [("(ILjava/math/BigInteger;)V", False), ("(ILjava/math/BigInteger;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    F0 = JavaStaticField("Ljava/math/BigInteger;")
    F4 = JavaStaticField("Ljava/math/BigInteger;")
    getKeysize = JavaMethod("()I")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getKeyParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")

class RSAPrivateCrtKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAPrivateCrtKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeQ = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentQ = JavaMethod("()Ljava/math/BigInteger;")
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")

class ECField(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECField"
    getFieldSize = JavaMethod("()I")

class XECPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/XECPublicKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/AlgorithmParameterSpec;Ljava/math/BigInteger;)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getU = JavaMethod("()Ljava/math/BigInteger;")

class InvalidParameterSpecException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/InvalidParameterSpecException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class ECFieldFp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECFieldFp"
    __javaconstructor__ = [("(Ljava/math/BigInteger;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getFieldSize = JavaMethod("()I")

class NamedParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/NamedParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    X25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    X448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ED25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ED448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    getName = JavaMethod("()Ljava/lang/String;")

class RSAOtherPrimeInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAOtherPrimeInfo"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getExponent = JavaMethod("()Ljava/math/BigInteger;")
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")
    getPrime = JavaMethod("()Ljava/math/BigInteger;")

class PSSParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/PSSParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;II)V", False), ("(I)V", False)]
    TRAILER_FIELD_BC = JavaStaticField("I")
    DEFAULT = JavaStaticField("Ljava/security/spec/PSSParameterSpec;")
    toString = JavaMethod("()Ljava/lang/String;")
    getDigestAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFAlgorithm = JavaMethod("()Ljava/lang/String;")
    getMGFParameters = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getSaltLength = JavaMethod("()I")
    getTrailerField = JavaMethod("()I")

class ECPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECPublicKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/ECPoint;Ljava/security/spec/ECParameterSpec;)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/ECParameterSpec;")
    getW = JavaMethod("()Ljava/security/spec/ECPoint;")

class EdDSAParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdDSAParameterSpec"
    __javaconstructor__ = [("(Z)V", False), ("(Z[B)V", False)]
    getContext = JavaMethod("()Ljava/util/Optional;")
    isPrehash = JavaMethod("()Z")

class EdECPoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdECPoint"
    __javaconstructor__ = [("(ZLjava/math/BigInteger;)V", False)]
    getY = JavaMethod("()Ljava/math/BigInteger;")
    isXOdd = JavaMethod("()Z")

class EncodedKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EncodedKeySpec"
    __javaconstructor__ = [("([B)V", False)]
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getFormat = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")

class DSAPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/DSAPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getX = JavaMethod("()Ljava/math/BigInteger;")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getQ = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")

class DSAPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/DSAPublicKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    getY = JavaMethod("()Ljava/math/BigInteger;")
    getP = JavaMethod("()Ljava/math/BigInteger;")
    getQ = JavaMethod("()Ljava/math/BigInteger;")
    getG = JavaMethod("()Ljava/math/BigInteger;")

class RSAMultiPrimePrivateCrtKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAMultiPrimePrivateCrtKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;[Ljava/security/spec/RSAOtherPrimeInfo;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/math/BigInteger;[Ljava/security/spec/RSAOtherPrimeInfo;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeQ = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentP = JavaMethod("()Ljava/math/BigInteger;")
    getPrimeExponentQ = JavaMethod("()Ljava/math/BigInteger;")
    getCrtCoefficient = JavaMethod("()Ljava/math/BigInteger;")
    getOtherPrimeInfo = JavaMethod("()[Ljava/security/spec/RSAOtherPrimeInfo;")

class InvalidKeySpecException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/InvalidKeySpecException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]

class PKCS8EncodedKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/PKCS8EncodedKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BLjava/lang/String;)V", False)]
    getFormat = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")

class X509EncodedKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/X509EncodedKeySpec"
    __javaconstructor__ = [("([B)V", False), ("([BLjava/lang/String;)V", False)]
    getFormat = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")

class RSAPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAPublicKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getPublicExponent = JavaMethod("()Ljava/math/BigInteger;")
    getModulus = JavaMethod("()Ljava/math/BigInteger;")

class ECGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECGenParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    X25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    X448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ED25519 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")
    ED448 = JavaStaticField("Ljava/security/spec/NamedParameterSpec;")

class EdECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/NamedParameterSpec;[B)V", False)]
    getBytes = JavaMethod("()[B")
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")

class EllipticCurve(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EllipticCurve"
    __javaconstructor__ = [("(Ljava/security/spec/ECField;Ljava/math/BigInteger;Ljava/math/BigInteger;[B)V", False), ("(Ljava/security/spec/ECField;Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getField = JavaMethod("()Ljava/security/spec/ECField;")
    getA = JavaMethod("()Ljava/math/BigInteger;")
    getB = JavaMethod("()Ljava/math/BigInteger;")
    getSeed = JavaMethod("()[B")

class DSAGenParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/DSAGenParameterSpec"
    __javaconstructor__ = [("(II)V", False), ("(III)V", False)]
    getPrimePLength = JavaMethod("()I")
    getSubprimeQLength = JavaMethod("()I")
    getSeedLength = JavaMethod("()I")

class ECFieldF2m(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECFieldF2m"
    __javaconstructor__ = [("(I[I)V", False), ("(ILjava/math/BigInteger;)V", False), ("(I)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getFieldSize = JavaMethod("()I")
    getM = JavaMethod("()I")
    getReductionPolynomial = JavaMethod("()Ljava/math/BigInteger;")
    getMidTermsOfReductionPolynomial = JavaMethod("()[I")

class ECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/security/spec/ECParameterSpec;)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/ECParameterSpec;")
    getS = JavaMethod("()Ljava/math/BigInteger;")

class ECPoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECPoint"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False)]
    POINT_INFINITY = JavaStaticField("Ljava/security/spec/ECPoint;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAffineX = JavaMethod("()Ljava/math/BigInteger;")
    getAffineY = JavaMethod("()Ljava/math/BigInteger;")

class AlgorithmParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/AlgorithmParameterSpec"

class XECPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/XECPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/AlgorithmParameterSpec;[B)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getScalar = JavaMethod("()[B")

class ECParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/ECParameterSpec"
    __javaconstructor__ = [("(Ljava/security/spec/EllipticCurve;Ljava/security/spec/ECPoint;Ljava/math/BigInteger;I)V", False)]
    getOrder = JavaMethod("()Ljava/math/BigInteger;")
    getCurve = JavaMethod("()Ljava/security/spec/EllipticCurve;")
    getGenerator = JavaMethod("()Ljava/security/spec/ECPoint;")
    getCofactor = JavaMethod("()I")

class KeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/KeySpec"

class MGF1ParameterSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/MGF1ParameterSpec"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    SHA1 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA224 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA256 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA384 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA512 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA512_224 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA512_256 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_224 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_256 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_384 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    SHA3_512 = JavaStaticField("Ljava/security/spec/MGF1ParameterSpec;")
    toString = JavaMethod("()Ljava/lang/String;")
    getDigestAlgorithm = JavaMethod("()Ljava/lang/String;")

class EdECPublicKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/EdECPublicKeySpec"
    __javaconstructor__ = [("(Ljava/security/spec/NamedParameterSpec;Ljava/security/spec/EdECPoint;)V", False)]
    getPoint = JavaMethod("()Ljava/security/spec/EdECPoint;")
    getParams = JavaMethod("()Ljava/security/spec/NamedParameterSpec;")

class RSAPrivateKeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/RSAPrivateKeySpec"
    __javaconstructor__ = [("(Ljava/math/BigInteger;Ljava/math/BigInteger;)V", False), ("(Ljava/math/BigInteger;Ljava/math/BigInteger;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
    getParams = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getModulus = JavaMethod("()Ljava/math/BigInteger;")
    getPrivateExponent = JavaMethod("()Ljava/math/BigInteger;")