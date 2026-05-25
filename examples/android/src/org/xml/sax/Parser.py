from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Parser"]

class Parser(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Parser"
    setLocale = JavaMethod("(Ljava/util/Locale;)V")
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    setDocumentHandler = JavaMethod("(Lorg/xml/sax/DocumentHandler;)V")
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    parse = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)V", False, False), ("(Ljava/lang/String;)V", False, False)])