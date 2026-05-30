from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class X500PrivateCredential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/x500/X500PrivateCredential"
    __javaconstructor__ = [("(Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;)V", False), ("(Ljava/security/cert/X509Certificate;Ljava/security/PrivateKey;Ljava/lang/String;)V", False)]
    getCertificate = JavaMethod("()Ljava/security/cert/X509Certificate;")
    getAlias = JavaMethod("()Ljava/lang/String;")
    getPrivateKey = JavaMethod("()Ljava/security/PrivateKey;")
    isDestroyed = JavaMethod("()Z")
    destroy = JavaMethod("()V")

class X500Principal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/x500/X500Principal"
    __javaconstructor__ = [("(Ljava/io/InputStream;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/util/Map;)V", False), ("([B)V", False)]
    RFC1779 = JavaStaticField("Ljava/lang/String;")
    RFC2253 = JavaStaticField("Ljava/lang/String;")
    CANONICAL = JavaStaticField("Ljava/lang/String;")
    getName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/util/Map;)Ljava/lang/String;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")