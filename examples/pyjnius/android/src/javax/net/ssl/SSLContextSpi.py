from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLContextSpi"]

class SSLContextSpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLContextSpi"
    __javaconstructor__ = [("()V", False)]