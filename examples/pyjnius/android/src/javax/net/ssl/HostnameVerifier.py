from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HostnameVerifier"]

class HostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/HostnameVerifier"
    verify = JavaMethod("(Ljava/lang/String;Ljavax/net/ssl/SSLSession;)Z")