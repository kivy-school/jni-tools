from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    createInstallIntent = JavaStaticMethod("()Landroid/content/Intent;")
    createManageCredentialsIntent = JavaStaticMethod("(Landroid/security/AppUriAuthenticationPolicy;)Landroid/content/Intent;")
    choosePrivateKeyAlias = JavaMultipleMethod([("(Landroid/app/Activity;Landroid/security/KeyChainAliasCallback;[Ljava/lang/String;[Ljava/security/Principal;Ljava/lang/String;ILjava/lang/String;)V", True, False), ("(Landroid/app/Activity;Landroid/security/KeyChainAliasCallback;[Ljava/lang/String;[Ljava/security/Principal;Landroid/net/Uri;Ljava/lang/String;)V", True, False)])
    isCredentialManagementApp = JavaStaticMethod("(Landroid/content/Context;)Z")
    getCredentialManagementAppPolicy = JavaStaticMethod("(Landroid/content/Context;)Landroid/security/AppUriAuthenticationPolicy;")
    removeCredentialManagementApp = JavaStaticMethod("(Landroid/content/Context;)Z")
    getPrivateKey = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Ljava/security/PrivateKey;")
    getCertificateChain = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)[Ljava/security/cert/X509Certificate;")
    isKeyAlgorithmSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    isBoundKeyAlgorithm = JavaStaticMethod("(Ljava/lang/String;)Z")