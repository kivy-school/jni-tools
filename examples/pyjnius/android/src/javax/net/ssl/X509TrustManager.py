from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509TrustManager"]

class X509TrustManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509TrustManager"
    checkServerTrusted = JavaMethod("([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V")
    checkClientTrusted = JavaMethod("([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V")
    getAcceptedIssuers = JavaMethod("()[Ljava/security/cert/X509Certificate;")