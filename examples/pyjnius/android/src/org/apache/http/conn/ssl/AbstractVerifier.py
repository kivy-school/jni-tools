from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractVerifier"]

class AbstractVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/AbstractVerifier"
    __javaconstructor__ = [("()V", False)]
    getDNSSubjectAlts = JavaStaticMethod("(Ljava/security/cert/X509Certificate;)[Ljava/lang/String;")
    getCNs = JavaStaticMethod("(Ljava/security/cert/X509Certificate;)[Ljava/lang/String;")
    acceptableCountryWildcard = JavaStaticMethod("(Ljava/lang/String;)Z")
    countDots = JavaStaticMethod("(Ljava/lang/String;)I")
    verify = JavaMultipleMethod([("(Ljava/lang/String;Ljavax/net/ssl/SSLSocket;)V", False, False), ("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z", False, False), ("(Ljava/lang/String;Ljava/security/cert/X509Certificate;)V", False, False), ("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;Z)V", False, False)])