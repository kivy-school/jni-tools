from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureRandomSpi"]

class SecureRandomSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandomSpi"
    __javaconstructor__ = [("()V", False), ("(Ljava/security/SecureRandomParameters;)V", False)]
    engineSetSeed = JavaMethod("([B)V")
    engineNextBytes = JavaMultipleMethod([("([B)V", False, False), ("([BLjava/security/SecureRandomParameters;)V", False, False)])
    engineGenerateSeed = JavaMethod("(I)[B")
    engineReseed = JavaMethod("(Ljava/security/SecureRandomParameters;)V")
    engineGetParameters = JavaMethod("()Ljava/security/SecureRandomParameters;")
    toString = JavaMethod("()Ljava/lang/String;")