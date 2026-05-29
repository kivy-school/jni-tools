from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXTransformerFactory"]

class SAXTransformerFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/sax/SAXTransformerFactory"
    FEATURE = JavaStaticField("Ljava/lang/String;")
    FEATURE_XMLFILTER = JavaStaticField("Ljava/lang/String;")
    newTransformerHandler = JavaMultipleMethod([("()Ljavax/xml/transform/sax/TransformerHandler;", False, False), ("(Ljavax/xml/transform/Templates;)Ljavax/xml/transform/sax/TransformerHandler;", False, False), ("(Ljavax/xml/transform/Source;)Ljavax/xml/transform/sax/TransformerHandler;", False, False)])
    newTemplatesHandler = JavaMethod("()Ljavax/xml/transform/sax/TemplatesHandler;")
    newXMLFilter = JavaMultipleMethod([("(Ljavax/xml/transform/Templates;)Lorg/xml/sax/XMLFilter;", False, False), ("(Ljavax/xml/transform/Source;)Lorg/xml/sax/XMLFilter;", False, False)])