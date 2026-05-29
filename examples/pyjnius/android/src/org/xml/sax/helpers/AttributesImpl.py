from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributesImpl"]

class AttributesImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/AttributesImpl"
    __javaconstructor__ = [("(Lorg/xml/sax/Attributes;)V", False), ("()V", False)]
    removeAttribute = JavaMethod("(I)V")
    getLength = JavaMethod("()I")
    clear = JavaMethod("()V")
    getValue = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    setValue = JavaMethod("(ILjava/lang/String;)V")
    getType = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    setType = JavaMethod("(ILjava/lang/String;)V")
    setAttribute = JavaMethod("(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    setAttributes = JavaMethod("(Lorg/xml/sax/Attributes;)V")
    getURI = JavaMethod("(I)Ljava/lang/String;")
    getLocalName = JavaMethod("(I)Ljava/lang/String;")
    getQName = JavaMethod("(I)Ljava/lang/String;")
    setURI = JavaMethod("(ILjava/lang/String;)V")
    setLocalName = JavaMethod("(ILjava/lang/String;)V")
    setQName = JavaMethod("(ILjava/lang/String;)V")
    addAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    getIndex = JavaMultipleMethod([("(Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;Ljava/lang/String;)I", False, False)])