from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLFilter"]

class XMLFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/XMLFilter"
    getParent = JavaMethod("()Lorg/xml/sax/XMLReader;")
    setParent = JavaMethod("(Lorg/xml/sax/XMLReader;)V")