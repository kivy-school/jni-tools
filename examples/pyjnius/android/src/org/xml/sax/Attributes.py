from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Attributes"]

class Attributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/Attributes"
    getLength = JavaMethod("()I")
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getType = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    getURI = JavaMethod("(I)Ljava/lang/String;")
    getLocalName = JavaMethod("(I)Ljava/lang/String;")
    getQName = JavaMethod("(I)Ljava/lang/String;")
    getIndex = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;Ljava/lang/String;)I", False, False)])