from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSSerializer"]

class LSSerializer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSSerializer"
    getDomConfig = JavaMethod("()Lorg/w3c/dom/DOMConfiguration;")
    getNewLine = JavaMethod("()Ljava/lang/String;")
    setNewLine = JavaMethod("(Ljava/lang/String;)V")
    write = JavaMethod("(Lorg/w3c/dom/Node;Lorg/w3c/dom/ls/LSOutput;)Z")
    writeToURI = JavaMethod("(Lorg/w3c/dom/Node;Ljava/lang/String;)Z")
    writeToString = JavaMethod("(Lorg/w3c/dom/Node;)Ljava/lang/String;")