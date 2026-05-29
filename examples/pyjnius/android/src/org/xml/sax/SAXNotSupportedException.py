from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXNotSupportedException"]

class SAXNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXNotSupportedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]