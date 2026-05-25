from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyStoreSpi"]

class KeyStoreSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/KeyStoreSpi"
    __javaconstructor__ = [("()V", False)]
    engineGetKey = JavaMethod("(Ljava/lang/String;[C)Ljava/security/Key;")
    engineGetCertificateChain = JavaMethod("(Ljava/lang/String;)[Ljava/security/cert/Certificate;")
    engineGetCertificate = JavaMethod("(Ljava/lang/String;)Ljava/security/cert/Certificate;")
    engineGetCreationDate = JavaMethod("(Ljava/lang/String;)Ljava/util/Date;")
    engineSetKeyEntry = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Key;[C[Ljava/security/cert/Certificate;)V", False, False), ("(Ljava/lang/String;[B[Ljava/security/cert/Certificate;)V", False, False)])
    engineSetCertificateEntry = JavaMethod("(Ljava/lang/String;Ljava/security/cert/Certificate;)V")
    engineDeleteEntry = JavaMethod("(Ljava/lang/String;)V")
    engineAliases = JavaMethod("()Ljava/util/Enumeration;")
    engineContainsAlias = JavaMethod("(Ljava/lang/String;)Z")
    engineSize = JavaMethod("()I")
    engineIsKeyEntry = JavaMethod("(Ljava/lang/String;)Z")
    engineIsCertificateEntry = JavaMethod("(Ljava/lang/String;)Z")
    engineGetCertificateAlias = JavaMethod("(Ljava/security/cert/Certificate;)Ljava/lang/String;")
    engineStore = JavaMultipleMethod([("(Ljava/io/OutputStream;[C)V", False, False), ("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False)])
    engineLoad = JavaMultipleMethod([("(Ljava/io/InputStream;[C)V", False, False), ("(Ljava/security/KeyStore$LoadStoreParameter;)V", False, False)])
    engineGetEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$ProtectionParameter;)Ljava/security/KeyStore$Entry;")
    engineSetEntry = JavaMethod("(Ljava/lang/String;Ljava/security/KeyStore$Entry;Ljava/security/KeyStore$ProtectionParameter;)V")
    engineEntryInstanceOf = JavaMethod("(Ljava/lang/String;Ljava/lang/Class;)Z")
    engineProbe = JavaMethod("(Ljava/io/InputStream;)Z")