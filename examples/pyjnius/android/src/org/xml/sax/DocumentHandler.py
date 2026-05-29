from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DocumentHandler"]

class DocumentHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/DocumentHandler"
    endDocument = JavaMethod("()V")
    ignorableWhitespace = JavaMethod("([CII)V")
    processingInstruction = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    startDocument = JavaMethod("()V")
    characters = JavaMethod("([CII)V")
    setDocumentLocator = JavaMethod("(Lorg/xml/sax/Locator;)V")
    startElement = JavaMethod("(Ljava/lang/String;Lorg/xml/sax/AttributeList;)V")
    endElement = JavaMethod("(Ljava/lang/String;)V")