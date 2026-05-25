from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMResult"]

class DOMResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMResult"
    __javaconstructor__ = [("()V", False), ("(Lorg/w3c/dom/Node;)V", False), ("(Lorg/w3c/dom/Node;Ljava/lang/String;)V", False), ("(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;)V", False), ("(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    setNode = JavaMethod("(Lorg/w3c/dom/Node;)V")
    getNode = JavaMethod("()Lorg/w3c/dom/Node;")
    setNextSibling = JavaMethod("(Lorg/w3c/dom/Node;)V")
    getNextSibling = JavaMethod("()Lorg/w3c/dom/Node;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")