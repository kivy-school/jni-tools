from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DOMResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMResult"
    __javaconstructor__ = [("()V", False), ("(Lorg/w3c/dom/Node;)V", False), ("(Lorg/w3c/dom/Node;Ljava/lang/String;)V", False), ("(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;)V", False), ("(Lorg/w3c/dom/Node;Lorg/w3c/dom/Node;Ljava/lang/String;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    PI_DISABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    PI_ENABLE_OUTPUT_ESCAPING = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    setNextSibling = JavaMethod("(Lorg/w3c/dom/Node;)V")
    getNextSibling = JavaMethod("()Lorg/w3c/dom/Node;")
    getNode = JavaMethod("()Lorg/w3c/dom/Node;")
    setNode = JavaMethod("(Lorg/w3c/dom/Node;)V")

class DOMLocator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMLocator"
    getOriginatingNode = JavaMethod("()Lorg/w3c/dom/Node;")

class DOMSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/xml/transform/dom/DOMSource"
    __javaconstructor__ = [("()V", False), ("(Lorg/w3c/dom/Node;Ljava/lang/String;)V", False), ("(Lorg/w3c/dom/Node;)V", False)]
    FEATURE = JavaStaticField("Ljava/lang/String;")
    getSystemId = JavaMethod("()Ljava/lang/String;")
    setSystemId = JavaMethod("(Ljava/lang/String;)V")
    isEmpty = JavaMethod("()Z")
    getNode = JavaMethod("()Lorg/w3c/dom/Node;")
    setNode = JavaMethod("(Lorg/w3c/dom/Node;)V")