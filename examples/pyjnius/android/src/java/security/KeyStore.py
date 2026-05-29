from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyStore"]

class KeyStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyStore"
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    size = JavaMethod("()I")
    load = JavaMultipleMethod([("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False), ("(Ljava/io/InputStream;[C)V", False, False)])
    store = JavaMultipleMethod([("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False), ("(Ljava/io/OutputStream;[C)V", False, False)])
    getKey = JavaMethod("(Ljava/lang/String;[C)Ljava/security/Key;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyStore;", True, False), ("(Ljava/io/File;Ljava/security/KeyStore$LoadStoreParameter;)Ljava/security/KeyStore;", True, False), ("(Ljava/io/File;[C)Ljava/security/KeyStore;", True, False), ("(Ljava/lang/String;)Ljava/security/KeyStore;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyStore;", True, False)])
    getType = JavaMethod("()Ljava/lang/String;")
    getAttributes = JavaMethod("(Ljava/lang/String;)Ljava/util/Set;")
    getCertificate = JavaMethod("(Ljava/lang/String;)Ljava/security/cert/Certificate;")
    getCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/Certificate;")
    aliases = JavaMethod("()Ljava/util/Enumeration;")
    isCertificateEntry = JavaMethod("(Ljava/lang/String;)Z")
    getCreationDate = JavaMethod("(Ljava/lang/String;)Ljava/util/Date;")
    setKeyEntry = JavaMultipleMethod([("(Ljava/lang/String;[B[Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/lang/String;Ljava/security/Key;[C[Ljava/security/cert/Certificate;)V", False, False)])
    setCertificateEntry = JavaMethod("(Ljava/lang/String;Ljava/security/cert/Certificate;)V")
    containsAlias = JavaMethod("(Ljava/lang/String;)Z")
    isKeyEntry = JavaMethod("(Ljava/lang/String;)Z")
    getCertificateAlias = JavaMethod("(Ljava/security/cert/Certificate;)Ljava/lang/String;")
    setEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$Entry;Ljava/security/KeyStore$ProtectionParameter;)V")
    entryInstanceOf = JavaMethod("(Ljava/lang/String;Ljava/lang/Class;)Z")
    getEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Entry;")
    deleteEntry = JavaMethod("(Ljava/lang/String;)V")

    class LoadStoreParameter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$LoadStoreParameter"
        getProtectionParameter = JavaMethod("()Ljava/security/KeyStore$ProtectionParameter;")

    class ProtectionParameter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$ProtectionParameter"

    class Entry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$Entry"
        getAttributes = JavaMethod("()Ljava/util/Set;")

        class Attribute(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "java/security/KeyStore$Entry$Attribute"
            getName = JavaMethod("()Ljava/lang/String;")
            getValue = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$Builder"
        getProtectionParameter = JavaMethod("(Ljava/lang/String;)Ljava/security/KeyStore$ProtectionParameter;")
        newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Provider;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/io/File;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;Ljava/io/File;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/security/KeyStore;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False)])
        getKeyStore = JavaMethod("()Ljava/security/KeyStore;")

    class TrustedCertificateEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$TrustedCertificateEntry"
        __javaconstructor__ = [("(Ljava/security/cert/Certificate;)V", False), ("(Ljava/security/cert/Certificate;Ljava/util/Set;)V", False)]
        getTrustedCertificate = JavaMethod("()Ljava/security/cert/Certificate;")
        toString = JavaMethod("()Ljava/lang/String;")
        getAttributes = JavaMethod("()Ljava/util/Set;")

    class SecretKeyEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$SecretKeyEntry"
        __javaconstructor__ = [("(Ljavax/crypto/SecretKey;)V", False), ("(Ljavax/crypto/SecretKey;Ljava/util/Set;)V", False)]
        getSecretKey = JavaMethod("()Ljavax/crypto/SecretKey;")
        toString = JavaMethod("()Ljava/lang/String;")
        getAttributes = JavaMethod("()Ljava/util/Set;")

    class PrivateKeyEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$PrivateKeyEntry"
        __javaconstructor__ = [("(Ljava/security/PrivateKey;[Ljava/security/cert/Certificate;)V", False), ("(Ljava/security/PrivateKey;[Ljava/security/cert/Certificate;Ljava/util/Set;)V", False)]
        getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
        toString = JavaMethod("()Ljava/lang/String;")
        getAttributes = JavaMethod("()Ljava/util/Set;")
        getCertificate = JavaMethod("()Ljava/security/cert/Certificate;")
        getCertificateChain = JavaMethod("()[Ljava/security/cert/Certificate;")

    class CallbackHandlerProtection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$CallbackHandlerProtection"
        __javaconstructor__ = [("(Ljavax/security/auth/callback/CallbackHandler;)V", False)]
        getCallbackHandler = JavaMethod("()Ljavax/security/auth/callback/CallbackHandler;")

    class PasswordProtection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore$PasswordProtection"
        __javaconstructor__ = [("([CLjava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;)V", False), ("([C)V", False)]
        getProtectionAlgorithm = JavaMethod("()Ljava/lang/String;")
        getPassword = JavaMethod("()[C")
        isDestroyed = JavaMethod("()Z")
        destroy = JavaMethod("()V")
        getProtectionParameters = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")