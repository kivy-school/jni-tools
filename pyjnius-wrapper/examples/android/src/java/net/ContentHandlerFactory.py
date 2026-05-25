from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentHandlerFactory"]

class ContentHandlerFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ContentHandlerFactory"
    createContentHandler = JavaMethod("(Ljava/lang/String;)Ljava/net/ContentHandler;")