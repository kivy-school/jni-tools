from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SslCertificate"]

class SslCertificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/SslCertificate"
    __javaconstructor__ = [("(Ljava/security/cert/X509Certificate;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Date;Ljava/util/Date;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    restoreState = JavaStaticMethod("(Landroid/os/Bundle;)Landroid/net/http/SslCertificate;")
    saveState = JavaStaticMethod("(Landroid/net/http/SslCertificate;)Landroid/os/Bundle;")
    getIssuedTo = JavaMethod("()Landroid/net/http/SslCertificate$DName;")
    getValidNotAfter = JavaMethod("()Ljava/lang/String;")
    getIssuedBy = JavaMethod("()Landroid/net/http/SslCertificate$DName;")
    getValidNotAfterDate = JavaMethod("()Ljava/util/Date;")
    getValidNotBefore = JavaMethod("()Ljava/lang/String;")
    getValidNotBeforeDate = JavaMethod("()Ljava/util/Date;")
    getX509Certificate = JavaMethod("()Ljava/security/cert/X509Certificate;")

    class DName(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/SslCertificate$DName"
        __javaconstructor__ = [("(Landroid/net/http/SslCertificate;Ljava/lang/String;)V", False)]
        getUName = JavaMethod("()Ljava/lang/String;")
        getCName = JavaMethod("()Ljava/lang/String;")
        getDName = JavaMethod("()Ljava/lang/String;")
        getOName = JavaMethod("()Ljava/lang/String;")