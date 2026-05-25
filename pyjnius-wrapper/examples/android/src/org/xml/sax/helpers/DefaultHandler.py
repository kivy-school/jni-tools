from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DefaultHandler"]

class DefaultHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/DefaultHandler"
    __javaconstructor__ = [("()V", False)]
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    notationDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    unparsedEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
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
    warning = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    error = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    fatalError = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")