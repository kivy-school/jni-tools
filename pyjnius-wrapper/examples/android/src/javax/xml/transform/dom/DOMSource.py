from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DOMSource"]

class DOMSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMSource"
    __javaconstructor__ = [("()V", False), ("(Lorg/w3c/dom/Node;)V", False), ("(Lorg/w3c/dom/Node;Ljava/lang/String;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    setNode = JavaMethod("(Lorg/w3c/dom/Node;)V")
    getNode = JavaMethod("()Lorg/w3c/dom/Node;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    getSystemId = JavaMethod("()Ljava/lang/String;")