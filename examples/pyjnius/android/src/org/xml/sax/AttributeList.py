from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeList"]

class AttributeList(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/AttributeList"
    getLength = JavaMethod("()I")
    getName = JavaMethod("(I)Ljava/lang/String;")
    getType = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])