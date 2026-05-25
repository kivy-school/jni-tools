from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentBuilder"]

class DocumentBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/parsers/DocumentBuilder"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    parse = JavaMultipleMethod([("(Ljava/io/InputStream;)Lorg/w3c/dom/Document;", False, False), ("(Ljava/io/InputStream;Ljava/lang/String;)Lorg/w3c/dom/Document;", False, False), ("(Ljava/lang/String;)Lorg/w3c/dom/Document;", False, False), ("(Ljava/io/File;)Lorg/w3c/dom/Document;", False, False), ("(Lorg/xml/sax/InputSource;)Lorg/w3c/dom/Document;", False, False)])
    isNamespaceAware = JavaMethod("()Z")
    isValidating = JavaMethod("()Z")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    newDocument = JavaMethod("()Lorg/w3c/dom/Document;")
    getDOMImplementation = JavaMethod("()Lorg/w3c/dom/DOMImplementation;")
    getSchema = JavaMethod("()Ljavax/xml/validation/Schema;")
    isXIncludeAware = JavaMethod("()Z")