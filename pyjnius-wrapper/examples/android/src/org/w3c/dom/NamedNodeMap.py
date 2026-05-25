from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamedNodeMap"]

class NamedNodeMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/NamedNodeMap"
    getNamedItem = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Node;")
    setNamedItem = JavaMethod("(Lorg/w3c/dom/Node;)Lorg/w3c/dom/Node;")
    removeNamedItem = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Node;")
    item = JavaMethod("(I)Lorg/w3c/dom/Node;")
    getLength = JavaMethod("()I")
    getNamedItemNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/Node;")
    setNamedItemNS = JavaMethod("(Lorg/w3c/dom/Node;)Lorg/w3c/dom/Node;")
    removeNamedItemNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/Node;")