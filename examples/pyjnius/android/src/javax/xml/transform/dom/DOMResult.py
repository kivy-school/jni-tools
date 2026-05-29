from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMResult"]

class DOMResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMResult"
    __javaconstructor__ = [("(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;)V", False), ("(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;)V", False), ("()V", False), ("(Lorg/w3c/dom/Node;Ljava/lang/String;)V", False), ("(Lorg/w3c/dom/Node;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    getNode = JavaMethod("()Lorg/w3c/dom/Node;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    setNextSibling = JavaMethod("(Lorg/w3c/dom/Node;)V")
    getNextSibling = JavaMethod("()Lorg/w3c/dom/Node;")
    setNode = JavaMethod("(Lorg/w3c/dom/Node;)V")