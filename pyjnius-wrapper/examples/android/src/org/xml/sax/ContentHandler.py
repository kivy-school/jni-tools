from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentHandler"]

class ContentHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ContentHandler"
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