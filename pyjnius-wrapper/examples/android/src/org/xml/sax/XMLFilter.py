from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLFilter"]

class XMLFilter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/XMLFilter"
    setParent = JavaMethod("(Lorg/xml/sax/XMLReader;)V")
    getParent = JavaMethod("()Lorg/xml/sax/XMLReader;")