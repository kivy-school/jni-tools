from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParserFactory"]

class ParserFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/ParserFactory"
    makeParser = JavaMultipleMethod([("()Lorg/xml/sax/Parser;", True, False), ("(Ljava/lang/String;)Lorg/xml/sax/Parser;", True, False)])