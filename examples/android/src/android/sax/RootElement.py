from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RootElement"]

class RootElement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/sax/RootElement"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")