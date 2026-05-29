from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureRandom"]

class SecureRandom(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandom"
    __javaconstructor__ = [("()V", False), ("([B)V", False)]
    nextLong = JavaMethod("()J")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    toString = JavaMethod("()Ljava/lang/String;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/SecureRandomParameters;Ljava/security/Provider;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/SecureRandom;", True, False), ("(Ljava/lang/String;Ljava/security/SecureRandomParameters;)Ljava/security/SecureRandom;", True, False)])
    getParameters = JavaMethod("()Ljava/security/SecureRandomParameters;")
    getAlgorithm = JavaMethod("()Ljava/lang/String;")
    getSeed = JavaStaticMethod("(I)[B")
    setSeed = JavaMultipleMethod([("(J)V", False, False), ("([B)V", False, False)])
    nextBytes = JavaMultipleMethod([("([BLjava/security/SecureRandomParameters;)V", False, False), ("([B)V", False, False)])
    generateSeed = JavaMethod("(I)[B")
    getInstanceStrong = JavaStaticMethod("()Ljava/security/SecureRandom;")
    reseed = JavaMultipleMethod([("(Ljava/security/SecureRandomParameters;)V", False, False), ("()V", False, False)])