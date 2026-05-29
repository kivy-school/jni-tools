from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLEngines"]

class SSLEngines(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ssl/SSLEngines"
    isSupportedEngine = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;)Z")
    setUseSessionTickets = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;Z)V")
    exportKeyingMaterial = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;Ljava/lang/String;[BI)[B")