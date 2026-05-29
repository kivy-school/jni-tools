from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SslCertificate"]

class SslCertificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/SslCertificate"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Date;Ljava/util/Date;)V", False), ("(Ljava/security/cert/X509Certificate;)V", False)]
    saveState = JavaStaticMethod("(Landroid/net/http/SslCertificate;)Landroid/os/Bundle;")
    restoreState = JavaStaticMethod("(Landroid/os/Bundle;)Landroid/net/http/SslCertificate;")
    getValidNotBeforeDate = JavaMethod("()Ljava/util/Date;")
    getValidNotBefore = JavaMethod("()Ljava/lang/String;")
    getValidNotAfterDate = JavaMethod("()Ljava/util/Date;")
    getValidNotAfter = JavaMethod("()Ljava/lang/String;")
    getIssuedTo = JavaMethod("()Landroid/net/http/SslCertificate$DName;")
    getIssuedBy = JavaMethod("()Landroid/net/http/SslCertificate$DName;")
    getX509Certificate = JavaMethod("()Ljava/security/cert/X509Certificate;")
    toString = JavaMethod("()Ljava/lang/String;")

    class DName(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/SslCertificate/DName"
        __javaconstructor__ = [("(Landroid/net/http/SslCertificate;Ljava/lang/String;)V", False)]
        getDName = JavaMethod("()Ljava/lang/String;")
        getCName = JavaMethod("()Ljava/lang/String;")
        getOName = JavaMethod("()Ljava/lang/String;")
        getUName = JavaMethod("()Ljava/lang/String;")