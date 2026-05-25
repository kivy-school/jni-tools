from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMStringList"]

class DOMStringList(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMStringList"
    item = JavaMethod("(I)Ljava/lang/String;")
    getLength = JavaMethod("()I")
    contains = JavaMethod("(Ljava/lang/String;)Z")