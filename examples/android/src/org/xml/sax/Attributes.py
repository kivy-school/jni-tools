from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attributes"]

class Attributes(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Attributes"
    getLength = JavaMethod("()I")
    getURI = JavaMethod("(I)Ljava/lang/String;")
    getLocalName = JavaMethod("(I)Ljava/lang/String;")
    getQName = JavaMethod("(I)Ljava/lang/String;")
    getType = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getIndex = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;)I", False, False)])