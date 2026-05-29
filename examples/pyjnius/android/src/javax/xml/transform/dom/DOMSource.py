from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMSource"]

class DOMSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMSource"
    __javaconstructor__ = [("(Lorg/w3c/dom/Node;Ljava/lang/String;)V", False), ("(Lorg/w3c/dom/Node;)V", False), ("()V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    isEmpty = JavaMethod("()Z")
    getNode = JavaMethod("()Lorg/w3c/dom/Node;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    setNode = JavaMethod("(Lorg/w3c/dom/Node;)V")