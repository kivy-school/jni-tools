from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HostnameVerifier"]

class HostnameVerifier(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HostnameVerifier"
    verify = JavaMethod("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z")