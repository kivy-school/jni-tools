from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attributes2"]

class Attributes2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/ext/Attributes2"
    isSpecified = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False), ("(I)Z", False, False)])
    isDeclared = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])