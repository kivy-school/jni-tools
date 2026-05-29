from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentBuilderFactory"]

class DocumentBuilderFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/DocumentBuilderFactory"
    setSchema = JavaMethod("(Ljavax/xml/validation/Schema;)V")
    getSchema = JavaMethod("()Ljavax/xml/validation/Schema;")
    newInstance = JavaMultipleMethod([("()Ljavax/xml/parsers/DocumentBuilderFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/parsers/DocumentBuilderFactory;", True, False)])
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    newDefaultInstance = JavaStaticMethod("()Ljavax/xml/parsers/DocumentBuilderFactory;")
    setNamespaceAware = JavaMethod("(Z)V")
    newDefaultNSInstance = JavaStaticMethod("()Ljavax/xml/parsers/DocumentBuilderFactory;")
    newNSInstance = JavaMultipleMethod([("()Ljavax/xml/parsers/DocumentBuilderFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/parsers/DocumentBuilderFactory;", True, False)])
    setValidating = JavaMethod("(Z)V")
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")
    setXIncludeAware = JavaMethod("(Z)V")
    isXIncludeAware = JavaMethod("()Z")
    newDocumentBuilder = JavaMethod("()Ljavax/xml/parsers/DocumentBuilder;")
    setIgnoringElementContentWhitespace = JavaMethod("(Z)V")
    setExpandEntityReferences = JavaMethod("(Z)V")
    setIgnoringComments = JavaMethod("(Z)V")
    setCoalescing = JavaMethod("(Z)V")
    isIgnoringElementContentWhitespace = JavaMethod("()Z")
    isExpandEntityReferences = JavaMethod("()Z")
    isIgnoringComments = JavaMethod("()Z")
    isCoalescing = JavaMethod("()Z")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")