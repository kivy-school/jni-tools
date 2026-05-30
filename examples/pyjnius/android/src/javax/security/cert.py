from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CertificateNotYetValidException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateNotYetValidException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class X509Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/X509Certificate"
    __javaconstructor__ = [("()V", False)]
    getVersion = JavaMethod("()I")
    getInstance = JavaMultipleMethod([("(Ljava/io/InputStream;)Ljavax/security/cert/X509Certificate;", True, False), ("([B)Ljavax/security/cert/X509Certificate;", True, False)])
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")
    checkValidity = JavaMultipleMethod([("()V", False, False), ("(Ljava/util/Date;)V", False, False)])
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getSubjectDN = JavaMethod("()Ljava/security/Principal;")
    getNotBefore = JavaMethod("()Ljava/util/Date;")
    getNotAfter = JavaMethod("()Ljava/util/Date;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")

class CertificateEncodingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateEncodingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class CertificateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class CertificateExpiredException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateExpiredException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/Certificate"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getEncoded = JavaMethod("()[B")
    verify = JavaMultipleMethod([("(Ljava/security/PublicKey;Ljava/lang/String;)V", False, False), ("(Ljava/security/PublicKey;)V", False, False)])
    getPublicKey = JavaMethod("()Ljava/security/PublicKey;")

class CertificateParsingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateParsingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]