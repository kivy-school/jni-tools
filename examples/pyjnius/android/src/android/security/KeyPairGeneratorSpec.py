from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyPairGeneratorSpec"]

class KeyPairGeneratorSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyPairGeneratorSpec"
    getKeySize = JavaMethod("()I")
    getKeystoreAlias = JavaMethod("()Ljava/lang/String;")
    getKeyType = JavaMethod("()Ljava/lang/String;")
    getEndDate = JavaMethod("()Ljava/util/Date;")
    isEncryptionRequired = JavaMethod("()Z")
    getAlgorithmParameterSpec = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
    getContext = JavaMethod("()Landroid/content/Context;")
    getStartDate = JavaMethod("()Ljava/util/Date;")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getSubjectDN = JavaMethod("()Ljavax/security/auth/x500/X500Principal;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/KeyPairGeneratorSpec$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setAlias = JavaMethod("(Ljava/lang/String;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setEndDate = JavaMethod("(Ljava/util/Date;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setAlgorithmParameterSpec = JavaMethod("(Ljava/security/spec/AlgorithmParameterSpec;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setEncryptionRequired = JavaMethod("()Landroid/security/KeyPairGeneratorSpec$Builder;")
        setKeySize = JavaMethod("(I)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setKeyType = JavaMethod("(Ljava/lang/String;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setSerialNumber = JavaMethod("(Ljava/math/BigInteger;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setStartDate = JavaMethod("(Ljava/util/Date;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        setSubject = JavaMethod("(Ljavax/security/auth/x500/X500Principal;)Landroid/security/KeyPairGeneratorSpec$Builder;")
        build = JavaMethod("()Landroid/security/KeyPairGeneratorSpec;")