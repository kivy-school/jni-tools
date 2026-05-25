from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509TrustManager"]

class X509TrustManager(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509TrustManager"
    checkClientTrusted = JavaMethod("([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V")
    checkServerTrusted = JavaMethod("([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V")
    getAcceptedIssuers = JavaMethod("()[Ljava/security/cert/X509Certificate;")