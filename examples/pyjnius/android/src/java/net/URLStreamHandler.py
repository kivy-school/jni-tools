from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLStreamHandler"]

class URLStreamHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URLStreamHandler"
    __javaconstructor__ = [("()V", False)]