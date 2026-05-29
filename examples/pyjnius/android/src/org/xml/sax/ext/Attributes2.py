from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attributes2"]

class Attributes2(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Attributes2"
    isDeclared = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False)])
    isSpecified = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])