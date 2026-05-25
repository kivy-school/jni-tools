from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignatureSpi"]

class SignatureSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SignatureSpi"
    __javaconstructor__ = [("()V", False)]
    appRandom = JavaField("Ljava/security/SecureRandom;")
    engineInitVerify = JavaMethod("(Ljava/security/PublicKey;)V")
    engineInitSign = JavaMultipleMethod([("(Ljava/security/PrivateKey;)V", False, False), ("(Ljava/security/PrivateKey;Ljava/security/SecureRandom;)V", False, False)])
    engineUpdate = JavaMultipleMethod([("(B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    engineSign = JavaMultipleMethod([("()[B", False, False), ("([BII)I", False, False)])
    engineVerify = JavaMultipleMethod([("([B)Z", False, False), ("([BII)Z", False, False)])
    engineSetParameter = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/Object;)V", False, False), ("(Ljava/security/spec/AlgorithmParameterSpec;)V", False, False)])
    engineGetParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    engineGetParameter = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    clone = JavaMethod("()Ljava/lang/Object;")