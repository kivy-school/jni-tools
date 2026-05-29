from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NameList"]

class NameList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/NameList"
    getName = JavaMethod("(I)Ljava/lang/String;")
    getLength = JavaMethod("()I")
    contains = JavaMethod("(Ljava/lang/String;)Z")
    getNamespaceURI = JavaMethod("(I)Ljava/lang/String;")
    containsNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")