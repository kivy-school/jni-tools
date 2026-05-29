from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLStreamHandlerFactory"]

class URLStreamHandlerFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URLStreamHandlerFactory"
    createURLStreamHandler = JavaMethod("(Ljava/lang/String;)Ljava/net/URLStreamHandler;")