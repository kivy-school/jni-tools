from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SslError"]

class SslError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/SslError"
    __javaconstructor__ = [("(ILjava/security/cert/X509Certificate;Ljava/lang/String;)V", False), ("(ILjava/security/cert/X509Certificate;)V", False), ("(ILandroid/net/http/SslCertificate;Ljava/lang/String;)V", False), ("(ILandroid/net/http/SslCertificate;)V", False)]
    SSL_DATE_INVALID = JavaStaticField("I")
    SSL_EXPIRED = JavaStaticField("I")
    SSL_IDMISMATCH = JavaStaticField("I")
    SSL_INVALID = JavaStaticField("I")
    SSL_MAX_ERROR = JavaStaticField("I")
    SSL_NOTYETVALID = JavaStaticField("I")
    SSL_UNTRUSTED = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    addError = JavaMethod("(I)Z")
    getPrimaryError = JavaMethod("()I")
    getCertificate = JavaMethod("()Landroid/net/http/SslCertificate;")
    getUrl = JavaMethod("()Ljava/lang/String;")
    hasError = JavaMethod("(I)Z")