from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SAXNotRecognizedException"]

class SAXNotRecognizedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/SAXNotRecognizedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]