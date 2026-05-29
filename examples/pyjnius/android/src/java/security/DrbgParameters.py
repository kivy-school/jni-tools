from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrbgParameters"]

class DrbgParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DrbgParameters"
    nextBytes = JavaStaticMethod("(IZ[B)Ljava/security/DrbgParameters$NextBytes;")
    reseed = JavaStaticMethod("(Z[B)Ljava/security/DrbgParameters$Reseed;")
    instantiation = JavaStaticMethod("(ILjava/security/DrbgParameters$Capability;[B)Ljava/security/DrbgParameters$Instantiation;")

    class Instantiation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$Instantiation"
        getStrength = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        getCapability = JavaMethod("()Ljava/security/DrbgParameters$Capability;")
        getPersonalizationString = JavaMethod("()[B")

    class Capability(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$Capability"
        PR_AND_RESEED = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        RESEED_ONLY = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        NONE = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        toString = JavaMethod("()Ljava/lang/String;")
        values = JavaStaticMethod("()[Ljava/security/DrbgParameters$Capability;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/security/DrbgParameters$Capability;")
        supportsReseeding = JavaMethod("()Z")
        supportsPredictionResistance = JavaMethod("()Z")
        PR_AND_RESEED = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        RESEED_ONLY = JavaStaticField("Ljava/security/DrbgParameters$Capability;")
        NONE = JavaStaticField("Ljava/security/DrbgParameters$Capability;")

    class NextBytes(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$NextBytes"
        getStrength = JavaMethod("()I")
        getPredictionResistance = JavaMethod("()Z")
        getAdditionalInput = JavaMethod("()[B")

    class Reseed(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/DrbgParameters$Reseed"
        getPredictionResistance = JavaMethod("()Z")
        getAdditionalInput = JavaMethod("()[B")