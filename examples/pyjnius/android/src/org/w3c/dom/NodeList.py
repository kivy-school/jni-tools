from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NodeList"]

class NodeList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/NodeList"
    getLength = JavaMethod("()I")
    item = JavaMethod("(I)Lorg/w3c/dom/Node;")