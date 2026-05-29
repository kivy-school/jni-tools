from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXException"]

class SAXException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Exception;)V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    toString = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getException = JavaMethod("()Ljava/lang/Exception;")