from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractVerifier"]

class AbstractVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/AbstractVerifier"
    __javaconstructor__ = [("()V", False)]
    verify = JavaMultipleMethod([("(Ljava/lang/String;Ljavax/net/ssl/SSLSocket;)V", False, False), ("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z", False, False), ("(Ljava/lang/String;Ljava/security/cert/X509Certificate;)V", False, False), ("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;Z)V", False, False)])
    acceptableCountryWildcard = JavaStaticMethod("(Ljava/lang/String;)Z")
    getCNs = JavaStaticMethod("(Ljava/security/cert/X509Certificate;)[Ljava/lang/String;")
    getDNSSubjectAlts = JavaStaticMethod("(Ljava/security/cert/X509Certificate;)[Ljava/lang/String;")
    countDots = JavaStaticMethod("(Ljava/lang/String;)I")