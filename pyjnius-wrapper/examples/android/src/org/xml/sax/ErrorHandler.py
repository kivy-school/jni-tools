from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ErrorHandler"]

class ErrorHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ErrorHandler"
    warning = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    error = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")
    fatalError = JavaMethod("(Lorg/xml/sax/SAXParseException;)V")