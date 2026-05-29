from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLKeyException"]

class SSLKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLKeyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]