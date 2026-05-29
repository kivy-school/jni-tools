from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeList"]

class AttributeList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/AttributeList"
    getName = JavaMethod("(I)Ljava/lang/String;")
    getLength = JavaMethod("()I")
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getType = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])