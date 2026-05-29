from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509TrustManagerExtensions"]

class X509TrustManagerExtensions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/X509TrustManagerExtensions"
    __javaconstructor__ = [("(Ljavax/net/ssl/X509TrustManager;)V", False)]
    checkServerTrusted = JavaMultipleMethod([("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljava/lang/String;)Ljava/util/List;", False, False), ("([Ljava/security/cert/X509Certificate;[B[BLjava/lang/String;Ljava/lang/String;)Ljava/util/List;", False, False)])
    isSameTrustConfiguration = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    isUserAddedCertificate = JavaMethod("(Ljava/security/cert/X509Certificate;)Z")