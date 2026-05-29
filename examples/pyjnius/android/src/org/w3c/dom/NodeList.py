from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NodeList"]

class NodeList(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/NodeList"
    item = JavaMethod("(I)Lorg/w3c/dom/Node;")
    getLength = JavaMethod("()I")