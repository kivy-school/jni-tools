from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentHandler"]

class ContentHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ContentHandler"
    __javaconstructor__ = [("()V", False)]
    getContent = JavaMultipleMethod([("(Ljava/net/URLConnection;)Ljava/lang/Object;", False, False), ("(Ljava/net/URLConnection;[Ljava/lang/Class;)Ljava/lang/Object;", False, False)])