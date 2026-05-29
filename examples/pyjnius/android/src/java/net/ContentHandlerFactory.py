from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentHandlerFactory"]

class ContentHandlerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ContentHandlerFactory"
    createContentHandler = JavaMethod("(Ljava/lang/String;)Ljava/net/ContentHandler;")