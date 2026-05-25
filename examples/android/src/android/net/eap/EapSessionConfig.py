from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EapSessionConfig"]

class EapSessionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/eap/EapSessionConfig"
    getEapIdentity = JavaMethod("()[B")
    getEapSimConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapSimConfig;")
    getEapAkaConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaConfig;")
    getEapAkaPrimeConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaPrimeConfig;")
    getEapMsChapV2Config = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapMsChapV2Config;")
    getEapTtlsConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapTtlsConfig;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setEapIdentity = JavaMethod("([B)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapSimConfig = JavaMethod("(II)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapAkaConfig = JavaMultipleMethod([("(II)Landroid/net/eap/EapSessionConfig$Builder;", False, False), ("(IILandroid/net/eap/EapSessionConfig$EapAkaOption;)Landroid/net/eap/EapSessionConfig$Builder;", False, False)])
        setEapAkaPrimeConfig = JavaMethod("(IILjava/lang/String;Z)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapMsChapV2Config = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapTtlsConfig = JavaMethod("(Ljava/security/cert/X509Certificate;Landroid/net/eap/EapSessionConfig;)Landroid/net/eap/EapSessionConfig$Builder;")
        build = JavaMethod("()Landroid/net/eap/EapSessionConfig;")

    class EapAkaConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/EapAkaConfig"
        getEapAkaOption = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaOption;")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        getSubId = JavaMethod("()I")
        getAppType = JavaMethod("()I")

    class EapAkaOption(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/EapAkaOption"
        getReauthId = JavaMethod("()[B")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/net/eap/EapSessionConfig/EapAkaOption/Builder"
            __javaconstructor__ = [("()V", False)]
            setReauthId = JavaMethod("([B)Landroid/net/eap/EapSessionConfig$EapAkaOption$Builder;")
            build = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaOption;")

    class EapAkaPrimeConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/EapAkaPrimeConfig"
        getNetworkName = JavaMethod("()Ljava/lang/String;")
        allowsMismatchedNetworkNames = JavaMethod("()Z")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")

    class EapMethodConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/EapMethodConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getMethodType = JavaMethod("()I")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")

    class EapMsChapV2Config(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/EapMsChapV2Config"
        getUsername = JavaMethod("()Ljava/lang/String;")
        getPassword = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")

    class EapSimConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/EapSimConfig"
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        getSubId = JavaMethod("()I")
        getAppType = JavaMethod("()I")

    class EapTtlsConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig/EapTtlsConfig"
        getServerCaCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
        getInnerEapSessionConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig;")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")