from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Parser"]

class Parser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Parser"
    setErrorHandler = JavaMethod("(Lorg/xml/sax/ErrorHandler;)V")
    parse = JavaMultipleMethod([("(Lorg/xml/sax/InputSource;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    setEntityResolver = JavaMethod("(Lorg/xml/sax/EntityResolver;)V")
    setDTDHandler = JavaMethod("(Lorg/xml/sax/DTDHandler;)V")
    setLocale = JavaMethod("(Ljava/util/Locale;)V")
    setDocumentHandler = JavaMethod("(Lorg/xml/sax/DocumentHandler;)V")