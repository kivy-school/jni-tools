from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLSessionContext"]

class SSLSessionContext(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLSessionContext"
    getSession = JavaMethod("([B)Ljavax/net/ssl/SSLSession;")
    getIds = JavaMethod("()Ljava/util/Enumeration;")
    setSessionTimeout = JavaMethod("(I)V")
    getSessionTimeout = JavaMethod("()I")
    setSessionCacheSize = JavaMethod("(I)V")
    getSessionCacheSize = JavaMethod("()I")