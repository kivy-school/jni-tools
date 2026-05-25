from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Element"]

class Element(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/w3c/dom/Element"
    getTagName = JavaMethod("()Ljava/lang/String;")
    getAttribute = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    removeAttribute = JavaMethod("(Ljava/lang/String;)V")
    getAttributeNode = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/Attr;")
    setAttributeNode = JavaMethod("(Lorg/w3c/dom/Attr;)Lorg/w3c/dom/Attr;")
    removeAttributeNode = JavaMethod("(Lorg/w3c/dom/Attr;)Lorg/w3c/dom/Attr;")
    getElementsByTagName = JavaMethod("(Ljava/lang/String;)Lorg/w3c/dom/NodeList;")
    getAttributeNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    setAttributeNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    removeAttributeNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    getAttributeNodeNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/Attr;")
    setAttributeNodeNS = JavaMethod("(Lorg/w3c/dom/Attr;)Lorg/w3c/dom/Attr;")
    getElementsByTagNameNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lorg/w3c/dom/NodeList;")
    hasAttribute = JavaMethod("(Ljava/lang/String;)Z")
    hasAttributeNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    getSchemaTypeInfo = JavaMethod("()Lorg/w3c/dom/TypeInfo;")
    setIdAttribute = JavaMethod("(Ljava/lang/String;Z)V")
    setIdAttributeNS = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Z)V")
    setIdAttributeNode = JavaMethod("(Lorg/w3c/dom/Attr;Z)V")