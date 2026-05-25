from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509TrustManagerExtensions"]

class X509TrustManagerExtensions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/X509TrustManagerExtensions"
    __javaconstructor__ = [("(Ljavax/net/ssl/X509TrustManager;)V", False)]
    checkServerTrusted = JavaMethod("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljava/lang/String;)Ljava/util/List;")
    isUserAddedCertificate = JavaMethod("(Ljava/security/cert/X509Certificate;)Z")
    isSameTrustConfiguration = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")