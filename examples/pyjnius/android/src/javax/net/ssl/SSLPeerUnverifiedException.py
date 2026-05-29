from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLPeerUnverifiedException"]

class SSLPeerUnverifiedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLPeerUnverifiedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]