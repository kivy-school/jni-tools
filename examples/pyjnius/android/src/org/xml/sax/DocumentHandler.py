from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentHandler"]

class DocumentHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/DocumentHandler"
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startDocument = JavaMethod("()V")
    endDocument = JavaMethod("()V")
    startElement = JavaMethod("(Ljava/lang/String;Lorg/xml/sax/AttributeList;)V")
    endElement = JavaMethod("(Ljava/lang/String;)V")
    characters = JavaMethod("([CII)V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")