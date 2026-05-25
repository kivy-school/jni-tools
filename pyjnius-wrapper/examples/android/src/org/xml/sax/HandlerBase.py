from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandlerBase"]

class HandlerBase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/HandlerBase"
    __javaconstructor__ = [("()V", False)]
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    notationDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    unparsedEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startDocument = JavaMethod("()V")
    endDocument = JavaMethod("()V")
    startElement = JavaMethod("(Ljava/lang/String;Lorg/xml/sax/AttributeList;)V")
    endElement = JavaMethod("(Ljava/lang/String;)V")
    characters = JavaMethod("([CII)V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    warning = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    error = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    fatalError = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")