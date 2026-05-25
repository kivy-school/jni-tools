from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXException"]

class SAXException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;Ljava/lang/Exception;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")
    toString = JavaMethod("()Ljava/lang/String;")