from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureRandom"]

class SecureRandom(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandom"
    __javaconstructor__ = [("()V", False), ("([B)V", False), ("(Ljava/security/SecureRandomSpi;Ljava/security/Provider;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;Ljava/security/Provider;)Ljava/security/SecureRandom;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getParameters = JavaMethod("()Ljava/security/SecureRandomParameters;")
    setSeed = JavaMultipleMethod([("([B)V", False, False), ("(J)V", False, False)])
    nextBytes = JavaMultipleMethod([("([B)V", False, False), ("([BLjava/security/SecureRandomParameters;)V", False, False)])
    next = JavaMethod("(I)I")
    getSeed = JavaStaticMethod("(I)[B")
    generateSeed = JavaMethod("(I)[B")
    getInstanceStrong = JavaStaticMethod("()Ljava/security/SecureRandom;")
    reseed = JavaMultipleMethod([("()V", False, False), ("(Ljava/security/SecureRandomParameters;)V", False, False)])