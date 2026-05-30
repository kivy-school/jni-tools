from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Attributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Attributes"
    getURI = JavaMethod("(I)Ljava/lang/String;")
    getLocalName = JavaMethod("(I)Ljava/lang/String;")
    getQName = JavaMethod("(I)Ljava/lang/String;")
    getLength = JavaMethod("()I")
    getValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    getType = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getIndex = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;Ljava/lang/String;)I", False, False)])

class XMLFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/XMLFilter"
    getParent = JavaMethod("()Lorg/xml/sax/XMLReader;")
    setParent = JavaMethod("(Lorg/xml/sax/XMLReader;)V")

class SAXNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXNotSupportedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class Locator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Locator"
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getColumnNumber = JavaMethod("()I")
    getLineNumber = JavaMethod("()I")

class SAXNotRecognizedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXNotRecognizedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

class HandlerBase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/HandlerBase"
    __javaconstructor__ = [("()V", False)]
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    notationDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    unparsedEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startElement = JavaMethod("(Ljava/lang/String;Lorg/xml/sax/AttributeList;)V")
    endElement = JavaMethod("(Ljava/lang/String;)V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    endDocument = JavaMethod("()V")
    startDocument = JavaMethod("()V")
    characters = JavaMethod("([CII)V")
    warning = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    error = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    fatalError = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")

class ErrorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ErrorHandler"
    warning = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    error = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    fatalError = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")

class Parser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Parser"
    setDocumentHandler = JavaMethod("(Lorg/xml/sax/DocumentHandler;)V")
    parse = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    setLocale = JavaMethod("(Ljava/util/Locale;)V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")

class XMLReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/XMLReader"
    getErrorHandler = JavaMethod("()Lorg/xml/sax/ErrorHandler;")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setProperty = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    parse = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Lorg/xml/sax/InputSource;)V", False, False)])
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    getFeature = JavaMethod("(Ljava/lang/String;)Z")
    setFeature = JavaMethod("(Ljava/lang/String;Z)V")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    getEntityResolver = JavaMethod("()Lorg/xml/sax/EntityResolver;")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    getDTDHandler = JavaMethod("()Lorg/xml/sax/DTDHandler;")
    setContentHandler = JavaMethod("(Lorg/xml/sax/ContentHandler;)V")
    getContentHandler = JavaMethod("()Lorg/xml/sax/ContentHandler;")

class ContentHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ContentHandler"
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    declaration = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    startPrefixMapping = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    endPrefixMapping = JavaMethod("(Ljava/lang/String;)V")
    startElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V")
    endElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    skippedEntity = JavaMethod("(Ljava/lang/String;)V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    endDocument = JavaMethod("()V")
    startDocument = JavaMethod("()V")
    characters = JavaMethod("([CII)V")

class InputSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/InputSource"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/Reader;)V", False), ("(Ljava/io/InputStream;)V", False)]
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    setPublicId = JavaMethod("(Ljava/lang/String;)V")
    setByteStream = JavaMethod("(Ljava/io/InputStream;)V")
    getByteStream = JavaMethod("()Ljava/io/InputStream;")
    isEmpty = JavaMethod("()Z")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    setEncoding = JavaMethod("(Ljava/lang/String;)V")
    setCharacterStream = JavaMethod("(Ljava/io/Reader;)V")
    getCharacterStream = JavaMethod("()Ljava/io/Reader;")

class SAXException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Exception;)V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    toString = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")

class AttributeList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/AttributeList"
    getName = JavaMethod("(I)Ljava/lang/String;")
    getLength = JavaMethod("()I")
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getType = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])

class SAXParseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXParseException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IILjava/lang/Exception;)V", False), ("(Ljava/lang/String;Lorg/xml/sax/Locator;)V", False), ("(Ljava/lang/String;Lorg/xml/sax/Locator;Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;II)V", False)]
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getPublicId = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getColumnNumber = JavaMethod("()I")
    getLineNumber = JavaMethod("()I")

class DTDHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/DTDHandler"
    notationDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    unparsedEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")

class EntityResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/EntityResolver"
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")

class DocumentHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/DocumentHandler"
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startElement = JavaMethod("(Ljava/lang/String;Lorg/xml/sax/AttributeList;)V")
    endElement = JavaMethod("(Ljava/lang/String;)V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    endDocument = JavaMethod("()V")
    startDocument = JavaMethod("()V")
    characters = JavaMethod("([CII)V")