from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EapSessionConfig"]

class EapSessionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/eap/EapSessionConfig"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getEapAkaConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaConfig;")
    getEapIdentity = JavaMethod("()[B")
    getEapTtlsConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapTtlsConfig;")
    getEapSimConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapSimConfig;")
    getEapAkaPrimeConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaPrimeConfig;")
    getEapMsChapV2Config = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapMsChapV2Config;")

    class EapTtlsConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapTtlsConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getInnerEapSessionConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig;")
        getServerCaCert = JavaMethod("()Ljava/security/cert/X509Certificate;")

    class EapSimConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapSimConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getSubId = JavaMethod("()I")
        getAppType = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class EapMsChapV2Config(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapMsChapV2Config"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getPassword = JavaMethod("()Ljava/lang/String;")
        getUsername = JavaMethod("()Ljava/lang/String;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class EapMethodConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapMethodConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getMethodType = JavaMethod("()I")

    class EapAkaPrimeConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapAkaPrimeConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getNetworkName = JavaMethod("()Ljava/lang/String;")
        allowsMismatchedNetworkNames = JavaMethod("()Z")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class EapAkaOption(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapAkaOption"
        getReauthId = JavaMethod("()[B")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/net/eap/EapSessionConfig$EapAkaOption$Builder"
            __javaconstructor__ = [("()V", False)]
            build = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaOption;")
            setReauthId = JavaMethod("([B)Landroid/net/eap/EapSessionConfig$EapAkaOption$Builder;")

    class EapAkaConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapAkaConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getSubId = JavaMethod("()I")
        getEapAkaOption = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaOption;")
        getAppType = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setEapAkaConfig = JavaMultipleMethod([("(II)Landroid/net/eap/EapSessionConfig$Builder;", False, False), ("(IILandroid/net/eap/EapSessionConfig$EapAkaOption;)Landroid/net/eap/EapSessionConfig$Builder;", False, False)])
        setEapSimConfig = JavaMethod("(II)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapTtlsConfig = JavaMethod("(Ljava/security/cert/X509Certificate;Landroid/net/eap/EapSessionConfig;)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapIdentity = JavaMethod("([B)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapAkaPrimeConfig = JavaMethod("(IILjava/lang/String;Z)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapMsChapV2Config = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/eap/EapSessionConfig$Builder;")
        build = JavaMethod("()Landroid/net/eap/EapSessionConfig;")