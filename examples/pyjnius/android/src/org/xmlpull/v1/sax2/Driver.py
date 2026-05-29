from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Driver"]

class Driver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xmlpull/v1/sax2/Driver"
    __javaconstructor__ = [("()V", False), ("(Lorg/xmlpull/v1/XmlPullParser;)V", False)]
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    parseSubTree = JavaMethod("(Lorg/xmlpull/v1/XmlPullParser;)V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getLength = JavaMethod("()I")
    getValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    parse = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Lorg/xml/sax/InputSource;)V", False, False)])
    getType = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    getEntityResolver = JavaMethod("()Lorg/xml/sax/EntityResolver;")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    getDTDHandler = JavaMethod("()Lorg/xml/sax/DTDHandler;")
    setContentHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")
    getColumnNumber = JavaMethod("()I")
    getURI = JavaMethod("(I)Ljava/lang/String;")
    getLocalName = JavaMethod("(I)Ljava/lang/String;")
    getQName = JavaMethod("(I)Ljava/lang/String;")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getIndex = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    getLineNumber = JavaMethod("()I")