from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLHandshakeException"]

class SSLHandshakeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLHandshakeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]