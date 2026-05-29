from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HandlerBase"]

class HandlerBase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/HandlerBase"
    __javaconstructor__ = [("()V", False)]
    endDocument = JavaMethod("()V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    startDocument = JavaMethod("()V")
    warning = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    error = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    characters = JavaMethod("([CII)V")
    fatalError = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    notationDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    unparsedEntityDecl = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    resolveEntity = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/xml/sax/InputSource;")
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startElement = JavaMethod("(Ljava/lang/String;Lorg/xml/sax/AttributeList;)V")
    endElement = JavaMethod("(Ljava/lang/String;)V")