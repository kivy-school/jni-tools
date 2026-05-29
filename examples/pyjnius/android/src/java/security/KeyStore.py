from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyStore"]

class KeyStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyStore"
    __javaconstructor__ = [("(Ljava/security/KeyStoreSpi;Ljava/security/Provider;Ljava/lang/String;)V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/KeyStore;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/security/KeyStore;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;)Ljava/security/KeyStore;", True, False), ("(Ljava/io/File;[C)Ljava/security/KeyStore;", True, False), ("(Ljava/io/File;Ljava/security/KeyStore$LoadStoreParameter;)Ljava/security/KeyStore;", True, False)])
    getDefaultType = JavaStaticMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getType = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("(Ljava/lang/String;[C)Ljava/security/Key;")
    getCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/Certificate;")
    getCertificate = JavaMethod("(Ljava/lang/String;)Ljava/security/cert/Certificate;")
    getCreationDate = JavaMethod("(Ljava/lang/String;)Ljava/util/Date;")
    setKeyEntry = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Key;[C[Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/lang/String;[B[Ljava/security/cert/Certificate;)V", False, False)])
    setCertificateEntry = JavaMethod("(Ljava/lang/String;Ljava/security/cert/Certificate;)V")
    deleteEntry = JavaMethod("(Ljava/lang/String;)V")
    aliases = JavaMethod("()Ljava/util/Enumeration;")
    containsAlias = JavaMethod("(Ljava/lang/String;)Z")
    size = JavaMethod("()I")
    isKeyEntry = JavaMethod("(Ljava/lang/String;)Z")
    isCertificateEntry = JavaMethod("(Ljava/lang/String;)Z")
    getCertificateAlias = JavaMethod("(Ljava/security/cert/Certificate;)Ljava/lang/String;")
    store = JavaMultipleMethod([("(Ljava/io/OutputStream;[C)V", False, False), ("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False)])
    load = JavaMultipleMethod([("(Ljava/io/InputStream;[C)V", False, False), ("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False)])
    getEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Entry;")
    setEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$Entry;Ljava/security/KeyStore$ProtectionParameter;)V")
    entryInstanceOf = JavaMethod("(Ljava/lang/String;Ljava/lang/Class;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/Builder"
        __javaconstructor__ = [("()V", False)]
        getKeyStore = JavaMethod("()Ljava/security/KeyStore;")
        getProtectionParameter = JavaMethod("(Ljava/lang/String;)Ljava/security/KeyStore$ProtectionParameter;")
        newInstance = JavaMultipleMethod([("(Ljava/security/KeyStore;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;Ljava/io/File;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/io/File;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False), ("(Ljava/lang/String;Ljava/security/Provider;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Builder;", True, False)])

    class CallbackHandlerProtection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/CallbackHandlerProtection"
        __javaconstructor__ = [("(Ljavax/security/auth/callback/CallbackHandler;)V", False)]
        getCallbackHandler = JavaMethod("()Ljavax/security/auth/callback/CallbackHandler;")

    class Entry(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/Entry"
        getAttributes = JavaMethod("()Ljava/util/Set;")

        class Attribute(JavaInterface, metaclass=MetaJavaClass):
            __javaclass__ = "java/security/KeyStore/Entry/Attribute"
            getName = JavaMethod("()Ljava/lang/String;")
            getValue = JavaMethod("()Ljava/lang/String;")

    class LoadStoreParameter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/LoadStoreParameter"
        getProtectionParameter = JavaMethod("()Ljava/security/KeyStore$ProtectionParameter;")

    class PasswordProtection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/PasswordProtection"
        __javaconstructor__ = [("([C)V", False), ("([CLjava/lang/String;Ljava/security/spec/AlgorithmParameterSpec;)V", False)]
        getProtectionAlgorithm = JavaMethod("()Ljava/lang/String;")
        getProtectionParameters = JavaMethod("()Ljava/security/spec/AlgorithmParameterSpec;")
        getPassword = JavaMethod("()[C")
        destroy = JavaMethod("()V")
        isDestroyed = JavaMethod("()Z")

    class PrivateKeyEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/PrivateKeyEntry"
        __javaconstructor__ = [("(Ljava/security/PrivateKey;[Ljava/security/cert/Certificate;)V", False), ("(Ljava/security/PrivateKey;[Ljava/security/cert/Certificate;Ljava/util/Set;)V", False)]
        getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
        getCertificateChain = JavaMethod("()[Ljava/security/cert/Certificate;")
        getCertificate = JavaMethod("()Ljava/security/cert/Certificate;")
        getAttributes = JavaMethod("()Ljava/util/Set;")
        toString = JavaMethod("()Ljava/lang/String;")

    class ProtectionParameter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/ProtectionParameter"

    class SecretKeyEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/SecretKeyEntry"
        __javaconstructor__ = [("(Ljavax/crypto/SecretKey;)V", False), ("(Ljavax/crypto/SecretKey;Ljava/util/Set;)V", False)]
        getSecretKey = JavaMethod("()Ljavax/crypto/SecretKey;")
        getAttributes = JavaMethod("()Ljava/util/Set;")
        toString = JavaMethod("()Ljava/lang/String;")

    class TrustedCertificateEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/KeyStore/TrustedCertificateEntry"
        __javaconstructor__ = [("(Ljava/security/cert/Certificate;)V", False), ("(Ljava/security/cert/Certificate;Ljava/util/Set;)V", False)]
        getTrustedCertificate = JavaMethod("()Ljava/security/cert/Certificate;")
        getAttributes = JavaMethod("()Ljava/util/Set;")
        toString = JavaMethod("()Ljava/lang/String;")