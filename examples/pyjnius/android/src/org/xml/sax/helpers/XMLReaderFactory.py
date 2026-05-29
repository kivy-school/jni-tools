from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLReaderFactory"]

class XMLReaderFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/XMLReaderFactory"
    createXMLReader = JavaMultipleMethod([("()Lorg/xml/sax/XMLReader;", True, False), ("(Ljava/lang/String;)Lorg/xml/sax/XMLReader;", True, False)])