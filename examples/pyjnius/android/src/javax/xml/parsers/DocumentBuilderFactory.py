from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentBuilderFactory"]

class DocumentBuilderFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/DocumentBuilderFactory"
    __javaconstructor__ = [("()V", False)]
    newInstance = JavaMultipleMethod([("()Ljavax/xml/parsers/DocumentBuilderFactory;", True, False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljavax/xml/parsers/DocumentBuilderFactory;", True, False)])
    newDocumentBuilder = JavaMethod("()Ljavax/xml/parsers/DocumentBuilder;")
    setNamespaceAware = JavaMethod("(Z)V")
    setValidating = JavaMethod("(Z)V")
    setIgnoringElementContentWhitespace = JavaMethod("(Z)V")
    setExpandEntityReferences = JavaMethod("(Z)V")
    setIgnoringComments = JavaMethod("(Z)V")
    setCoalescing = JavaMethod("(Z)V")
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")
    isIgnoringElementContentWhitespace = JavaMethod("()Z")
    isExpandEntityReferences = JavaMethod("()Z")
    isIgnoringComments = JavaMethod("()Z")
    isCoalescing = JavaMethod("()Z")
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    getSchema = JavaMethod("()Ljavax/xml/validation/Schema;")
    setSchema = JavaMethod("(Ljavax/xml/validation/Schema;)V")
    setXIncludeAware = JavaMethod("(Z)V")
    isXIncludeAware = JavaMethod("()Z")