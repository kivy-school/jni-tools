from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NamedNodeMap"]

class NamedNodeMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/NamedNodeMap"
    getLength = JavaMethod("()I")
    getNamedItem = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Node;")
    setNamedItem = JavaMethod("(Lorg/w3c/dom/Node;)Lorg/w3c/dom/Node;")
    removeNamedItem = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Node;")
    getNamedItemNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/Node;")
    setNamedItemNS = JavaMethod("(Lorg/w3c/dom/Node;)Lorg/w3c/dom/Node;")
    removeNamedItemNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/Node;")
    item = JavaMethod("(I)Lorg/w3c/dom/Node;")