from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLReaderAdapter"]

class XMLReaderAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/XMLReaderAdapter"
    __javaconstructor__ = [("(Lorg/xml/sax/XMLReader;)V", False), ("()V", False)]
    endDocument = JavaMethod("()V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    startDocument = JavaMethod("()V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    parse = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    setLocale = JavaMethod("(Ljava/util/Locale;)V")
    characters = JavaMethod("([CII)V")
    setDocumentHandler = JavaMethod("(Lorg/xml/sax/DocumentHandler;)V")
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startPrefixMapping = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    endPrefixMapping = JavaMethod("(Ljava/lang/String;)V")
    startElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V")
    endElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    skippedEntity = JavaMethod("(Ljava/lang/String;)V")