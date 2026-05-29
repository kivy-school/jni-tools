from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLReader"]

class XMLReader(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/XMLReader"
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    getEntityResolver = JavaMethod("()Lorg/xml/sax/EntityResolver;")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    getDTDHandler = JavaMethod("()Lorg/xml/sax/DTDHandler;")
    setContentHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    parse = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)V", False, False), ("(Ljava/lang/String;)V", False, False)])