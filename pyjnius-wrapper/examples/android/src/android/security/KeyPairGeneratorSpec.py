from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyPairGeneratorSpec"]

class KeyPairGeneratorSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyPairGeneratorSpec"
    getContext = JavaMethod("()Landroid/content/Context;")
    getKeystoreAlias = JavaMethod("()Ljava/lang/String;")
    getKeyType = JavaMethod("()Ljava/lang/String;")
    getKeySize = JavaMethod("()I")
    getAlgorithmParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getSubjectDN = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getStartDate = JavaMethod("()Ljava/util/Date;")
    getEndDate = JavaMethod("()Ljava/util/Date;")
    isEncryptionRequired = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/KeyPairGeneratorSpec/Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setAlias = JavaMethod("(Ljava/lang/String;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setKeyType = JavaMethod("(Ljava/lang/String;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setKeySize = JavaMethod("(I)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setAlgorithmParameterSpec = JavaMethod("(Ljava/security/spec/AlgorithmParameterSpec;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setSubject = JavaMethod("(Ljavax/security/auth/x500/X500Principal;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setSerialNumber = JavaMethod("(Ljava/math/BigInteger;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setStartDate = JavaMethod("(Ljava/util/Date;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setEndDate = JavaMethod("(Ljava/util/Date;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setEncryptionRequired = JavaMethod("()Landroid/security/KeyPairGeneratorSpec$Builder;")
        build = JavaMethod("()Landroid/security/KeyPairGeneratorSpec;")