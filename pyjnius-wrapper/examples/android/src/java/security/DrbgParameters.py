from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrbgParameters"]

class DrbgParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DrbgParameters"
    instantiation = JavaStaticMethod("(ILjava/security/DrbgParameters$Capability;[B)Ljava/security/DrbgParameters$Instantiation;")
    nextBytes = JavaStaticMethod("(IZ[B)Ljava/security/DrbgParameters$NextBytes;")
    reseed = JavaStaticMethod("(Z[B)Ljava/security/DrbgParameters$Reseed;")

    class Capability(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters/Capability"
        values = JavaStaticMethod("()[Ljava/security/DrbgParameters$Capability;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/DrbgParameters$Capability;")
        toString = JavaMethod("()Ljava/lang/String;")
        supportsReseeding = JavaMethod("()Z")
        supportsPredictionResistance = JavaMethod("()Z")
        PR_AND_RESEED = JavaStaticField("Ljava/security/DrbgParameters/Capability;")
        RESEED_ONLY = JavaStaticField("Ljava/security/DrbgParameters/Capability;")
        NONE = JavaStaticField("Ljava/security/DrbgParameters/Capability;")

    class Instantiation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters/Instantiation"
        getStrength = JavaMethod("()I")
        getCapability = JavaMethod("()Ljava/security/DrbgParameters$Capability;")
        getPersonalizationString = JavaMethod("()[B")
        toString = JavaMethod("()Ljava/lang/String;")

    class NextBytes(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters/NextBytes"
        getStrength = JavaMethod("()I")
        getPredictionResistance = JavaMethod("()Z")
        getAdditionalInput = JavaMethod("()[B")

    class Reseed(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters/Reseed"
        getPredictionResistance = JavaMethod("()Z")
        getAdditionalInput = JavaMethod("()[B")