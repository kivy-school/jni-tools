from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentHandler"]

class ContentHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ContentHandler"
    endDocument = JavaMethod("()V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    startDocument = JavaMethod("()V")
    characters = JavaMethod("([CII)V")
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    declaration = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    startPrefixMapping = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    endPrefixMapping = JavaMethod("(Ljava/lang/String;)V")
    startElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lorg/xml/sax/Attributes;)V")
    endElement = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    skippedEntity = JavaMethod("(Ljava/lang/String;)V")