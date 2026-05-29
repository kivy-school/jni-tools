from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyChain"]

class KeyChain(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/KeyChain"
    __javaconstructor__ = [("()V", False)]
    ACTION_KEYCHAIN_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_KEY_ACCESS_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_STORAGE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_TRUST_STORE_CHANGED = JavaStaticField("Ljava/lang/String;")
    EXTRA_CERTIFICATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_KEY_ACCESSIBLE = JavaStaticField("Ljava/lang/String;")
    EXTRA_KEY_ALIAS = JavaStaticField("Ljava/lang/String;")
    EXTRA_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_PKCS12 = JavaStaticField("Ljava/lang/String;")
    KEY_ALIAS_SELECTION_DENIED = JavaStaticField("Ljava/lang/String;")
    choosePrivateKeyAlias = JavaMultipleMethod([("(Landroid/app/Activity;Landroid/security/KeyChainAliasCallback;[Ljava/lang/String;[Ljava/security/Principal;Ljava/lang/String;ILjava/lang/String;)V", True, False), ("(Landroid/app/Activity;Landroid/security/KeyChainAliasCallback;[Ljava/lang/String;[Ljava/security/Principal;Landroid/net/Uri;Ljava/lang/String;)V", True, False)])
    createInstallIntent = JavaStaticMethod("()Landroid/content/Intent;")
    createManageCredentialsIntent = JavaStaticMethod("(Landroid/security/AppUriAuthenticationPolicy;)Landroid/content/Intent;")
    getCredentialManagementAppPolicy = JavaStaticMethod("(Landroid/content/Context;)Landroid/security/AppUriAuthenticationPolicy;")
    getPrivateKey = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Ljava/security/PrivateKey;")
    isBoundKeyAlgorithm = JavaStaticMethod("(Ljava/lang/String;)Z")
    isCredentialManagementApp = JavaStaticMethod("(Landroid/content/Context;)Z")
    isKeyAlgorithmSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    removeCredentialManagementApp = JavaStaticMethod("(Landroid/content/Context;)Z")
    getCertificateChain = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)[Ljava/security/cert/X509Certificate;")