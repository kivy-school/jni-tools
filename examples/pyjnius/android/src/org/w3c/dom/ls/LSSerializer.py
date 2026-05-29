from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LSSerializer"]

class LSSerializer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/ls/LSSerializer"
    write = JavaMethod("(Lorg/w3c/dom/Node;Lorg/w3c/dom/ls/LSOutput;)Z")
    setFilter = JavaMethod("(Lorg/w3c/dom/ls/LSSerializerFilter;)V")
    getFilter = JavaMethod("()Lorg/w3c/dom/ls/LSSerializerFilter;")
    getDomConfig = JavaMethod("()Lorg/w3c/dom/DOMConfiguration;")
    getNewLine = JavaMethod("()Ljava/lang/String;")
    setNewLine = JavaMethod("(Ljava/lang/String;)V")
    writeToURI = JavaMethod("(Lorg/w3c/dom/Node;Ljava/lang/String;)Z")
    writeToString = JavaMethod("(Lorg/w3c/dom/Node;)Ljava/lang/String;")