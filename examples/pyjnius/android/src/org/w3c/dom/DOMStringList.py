from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMStringList"]

class DOMStringList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/DOMStringList"
    getLength = JavaMethod("()I")
    contains = JavaMethod("(Ljava/lang/String;)Z")
    item = JavaMethod("(I)Ljava/lang/String;")