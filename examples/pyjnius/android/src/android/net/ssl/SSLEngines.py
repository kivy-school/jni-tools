from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLEngines"]

class SSLEngines(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ssl/SSLEngines"
    isSupportedEngine = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;)Z")
    exportKeyingMaterial = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;Ljava/lang/String;[BI)[B")
    setUseSessionTickets = JavaStaticMethod("(Ljavax/net/ssl/SSLEngine;Z)V")