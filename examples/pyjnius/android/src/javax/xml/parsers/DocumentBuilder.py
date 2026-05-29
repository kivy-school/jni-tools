from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentBuilder"]

class DocumentBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/DocumentBuilder"
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getSchema = JavaMethod("()Ljavax/xml/validation/Schema;")
    reset = JavaMethod("()V")
    parse = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)Lorg/w3c/dom/Document;", False, False), ("(Ljava/io/File;)Lorg/w3c/dom/Document;", False, False), ("(Ljava/io/InputStream;)Lorg/w3c/dom/Document;", False, False), ("(Ljava/io/InputStream;Ljava/lang/String;)Lorg/w3c/dom/Document;", False, False), ("(Ljava/lang/String;)Lorg/w3c/dom/Document;", False, False)])
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")
    isXIncludeAware = JavaMethod("()Z")
    newDocument = JavaMethod("()Lorg/w3c/dom/Document;")
    getDOMImplementation = JavaMethod("()Lorg/w3c/dom/DOMImplementation;")