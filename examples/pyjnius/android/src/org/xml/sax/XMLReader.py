from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLReader"]

class XMLReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/XMLReader"
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    parse = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Lorg/xml/sax/InputSource;)V", False, False)])
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    getEntityResolver = JavaMethod("()Lorg/xml/sax/EntityResolver;")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    getDTDHandler = JavaMethod("()Lorg/xml/sax/DTDHandler;")
    setContentHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")