from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXParserFactory"]

class SAXParserFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/SAXParserFactory"
    setSchema = JavaMethod("(Ljavax/xml/validation/Schema;)V")
    getSchema = JavaMethod("()Ljavax/xml/validation/Schema;")
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/parsers/SAXParserFactory;", True, False), ("()Ljavax/xml/parsers/SAXParserFactory;", True, False)])
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/parsers/SAXParserFactory;")
    setNamespaceAware = JavaMethod("(Z)V")
    newDefaultNSInstance = JavaStaticMethod("()Ljavax/xml/parsers/SAXParserFactory;")
    newNSInstance = JavaMultipleMethod([("()Ljavax/xml/parsers/SAXParserFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/parsers/SAXParserFactory;", True, False)])
    newSAXParser = JavaMethod("()Ljavax/xml/parsers/SAXParser;")
    setValidating = JavaMethod("(Z)V")
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")
    setXIncludeAware = JavaMethod("(Z)V")
    isXIncludeAware = JavaMethod("()Z")