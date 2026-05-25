from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXParserFactory"]

class SAXParserFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/SAXParserFactory"
    __javaconstructor__ = [("()V", False)]
    newInstance = JavaMultipleMethod([("()Ljavax/xml/parsers/SAXParserFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/parsers/SAXParserFactory;", True, False)])
    newSAXParser = JavaMethod("()Ljavax/xml/parsers/SAXParser;")
    setNamespaceAware = JavaMethod("(Z)V")
    setValidating = JavaMethod("(Z)V")
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    getSchema = JavaMethod("()Ljavax/xml/validation/Schema;")
    setSchema = JavaMethod("(Ljavax/xml/validation/Schema;)V")
    setXIncludeAware = JavaMethod("(Z)V")
    isXIncludeAware = JavaMethod("()Z")