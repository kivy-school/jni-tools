from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["XMLReaderAdapter"]

class XMLReaderAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/XMLReaderAdapter"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/XMLReader;)V", False)]
    setLocale = JavaMethod("(Ljava/util/Locale;)V")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    setDocumentHandler = JavaMethod("(Lorg/xml/sax/DocumentHandler;)V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    parse = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Lorg/xml/sax/InputSource;)V", False, False)])
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startDocument = JavaMethod("()V")
    endDocument = JavaMethod("()V")
    startPrefixMapping = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    endPrefixMapping = JavaMethod("(Ljava/lang/String;)V")
    startElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V")
    endElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    characters = JavaMethod("([CII)V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    skippedEntity = JavaMethod("(Ljava/lang/String;)V")