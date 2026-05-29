from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLStreamHandlerFactory"]

class URLStreamHandlerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URLStreamHandlerFactory"
    createURLStreamHandler = JavaMethod("(Ljava/lang/String;)Ljava/net/URLStreamHandler;")