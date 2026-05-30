from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class EapInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/eap/EapInfo"
    getEapMethodType = JavaMethod("()I")

class EapAkaInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/eap/EapAkaInfo"
    getReauthId = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapAkaInfo$Builder"
        __javaconstructor__ = [("()V", False)]
        setReauthId = JavaMethod("([B)Landroid/net/eap/EapAkaInfo$Builder;")
        build = JavaMethod("()Landroid/net/eap/EapAkaInfo;")

class EapSessionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/eap/EapSessionConfig"
    getEapIdentity = JavaMethod("()[B")
    getEapAkaConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaConfig;")
    getEapAkaPrimeConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaPrimeConfig;")
    getEapMsChapV2Config = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapMsChapV2Config;")
    getEapSimConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapSimConfig;")
    getEapTtlsConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapTtlsConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class EapTtlsConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapTtlsConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getInnerEapSessionConfig = JavaMethod("()Landroid/net/eap/EapSessionConfig;")
        getServerCaCert = JavaMethod("()Ljava/security/cert/X509Certificate;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class EapSimConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapSimConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getAppType = JavaMethod("()I")
        getSubId = JavaMethod("()I")
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
        getMethodType = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class EapAkaPrimeConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapAkaPrimeConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        allowsMismatchedNetworkNames = JavaMethod("()Z")
        getNetworkName = JavaMethod("()Ljava/lang/String;")
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
            setReauthId = JavaMethod("([B)Landroid/net/eap/EapSessionConfig$EapAkaOption$Builder;")
            build = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaOption;")

    class EapAkaConfig(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$EapAkaConfig"
        EAP_TYPE_AKA = JavaStaticField("I")
        EAP_TYPE_AKA_PRIME = JavaStaticField("I")
        EAP_TYPE_MSCHAP_V2 = JavaStaticField("I")
        EAP_TYPE_SIM = JavaStaticField("I")
        EAP_TYPE_TTLS = JavaStaticField("I")
        getAppType = JavaMethod("()I")
        getEapAkaOption = JavaMethod("()Landroid/net/eap/EapSessionConfig$EapAkaOption;")
        getSubId = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/eap/EapSessionConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setEapAkaConfig = JavaMultipleMethod([("(IILandroid/net/eap/EapSessionConfig$EapAkaOption;)Landroid/net/eap/EapSessionConfig$Builder;", False, False), ("(II)Landroid/net/eap/EapSessionConfig$Builder;", False, False)])
        setEapAkaPrimeConfig = JavaMethod("(IILjava/lang/String;Z)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapIdentity = JavaMethod("([B)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapMsChapV2Config = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapSimConfig = JavaMethod("(II)Landroid/net/eap/EapSessionConfig$Builder;")
        setEapTtlsConfig = JavaMethod("(Ljava/security/cert/X509Certificate;Landroid/net/eap/EapSessionConfig;)Landroid/net/eap/EapSessionConfig$Builder;")
        build = JavaMethod("()Landroid/net/eap/EapSessionConfig;")