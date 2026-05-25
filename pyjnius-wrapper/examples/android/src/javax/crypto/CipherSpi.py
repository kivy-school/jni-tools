from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CipherSpi"]

class CipherSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/CipherSpi"
    __javaconstructor__ = [("()V", False)]
    engineSetMode = JavaMethod("(Ljava/lang/String;)V")
    engineSetPadding = JavaMethod("(Ljava/lang/String;)V")
    engineGetBlockSize = JavaMethod("()I")
    engineGetOutputSize = JavaMethod("(I)I")
    engineGetIV = JavaMethod("()[B")
    engineGetParameters = JavaMethod("()Ljava/security/AlgorithmParameters;")
    engineInit = JavaMultipleMethod([("(ILjava/security/Key;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;Ljava/security/SecureRandom;)V", False, False), ("(ILjava/security/Key;Ljava/security/AlgorithmParameters;Ljava/security/SecureRandom;)V", False, False)])
    engineUpdate = JavaMultipleMethod([("([BII)[B", False, False), ("([BII[BI)I", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False)])
    engineDoFinal = JavaMultipleMethod([("([BII)[B", False, False), ("([BII[BI)I", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;)I", False, False)])
    engineWrap = JavaMethod("(Ljava/security/Key;)[B")
    engineUnwrap = JavaMethod("([BLjava/lang/String;I)Ljava/security/Key;")
    engineGetKeySize = JavaMethod("(Ljava/security/Key;)I")
    engineUpdateAAD = JavaMultipleMethod([("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])