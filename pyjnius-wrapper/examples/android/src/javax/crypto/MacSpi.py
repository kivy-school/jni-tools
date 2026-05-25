from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MacSpi"]

class MacSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/MacSpi"
    __javaconstructor__ = [("()V", False)]
    engineGetMacLength = JavaMethod("()I")
    engineInit = JavaMethod("(Ljava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V")
    engineUpdate = JavaMultipleMethod([("(B)V", False, False), ("([BII)V", False, False), ("(Ljava/nio/ByteBuffer;)V", False, False)])
    engineDoFinal = JavaMethod("()[B")
    engineReset = JavaMethod("()V")
    clone = JavaMethod("()Ljava/lang/Object;")