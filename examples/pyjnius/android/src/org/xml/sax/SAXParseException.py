from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXParseException"]

class SAXParseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXParseException"
    __javaconstructor__ = [("(Ljava/lang/String;Lorg/xml/sax/Locator;)V", False), ("(Ljava/lang/String;Lorg/xml/sax/Locator;Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;II)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IILjava/lang/Exception;)V", False)]
    getPublicId = JavaMethod("()Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")
    getColumnNumber = JavaMethod("()I")