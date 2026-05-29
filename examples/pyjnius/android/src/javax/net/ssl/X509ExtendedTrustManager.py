from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509ExtendedTrustManager"]

class X509ExtendedTrustManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/X509ExtendedTrustManager"
    __javaconstructor__ = [("()V", False)]
    checkServerTrusted = JavaMultipleMethod([("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljavax/net/ssl/SSLEngine;)V", False, False), ("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljava/net/Socket;)V", False, False)])
    checkClientTrusted = JavaMultipleMethod([("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljava/net/Socket;)V", False, False), ("([Ljava/security/cert/X509Certificate;Ljava/lang/String;Ljavax/net/ssl/SSLEngine;)V", False, False)])