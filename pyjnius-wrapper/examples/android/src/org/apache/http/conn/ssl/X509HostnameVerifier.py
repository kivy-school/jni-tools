from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509HostnameVerifier"]

class X509HostnameVerifier(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/X509HostnameVerifier"
    verify = JavaMultipleMethod([("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z", False, False), ("(Ljava/lang/String;Ljavax/net/ssl/SSLSocket;)V", False, False), ("(Ljava/lang/String;Ljava/security/cert/X509Certificate;)V", False, False), ("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V", False, False)])