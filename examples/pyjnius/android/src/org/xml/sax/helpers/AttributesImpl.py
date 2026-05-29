from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributesImpl"]

class AttributesImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/AttributesImpl"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/Attributes;)V", False)]
    getLength = JavaMethod("()I")
    getURI = JavaMethod("(I)Ljava/lang/String;")
    getLocalName = JavaMethod("(I)Ljava/lang/String;")
    getQName = JavaMethod("(I)Ljava/lang/String;")
    getType = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getIndex = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", False, False), ("(Ljava/lang/String;)I", False, False)])
    clear = JavaMethod("()V")
    setAttributes = JavaMethod("(Lorg/xml/sax/Attributes;)V")
    addAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    setAttribute = JavaMethod("(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    removeAttribute = JavaMethod("(I)V")
    setURI = JavaMethod("(ILjava/lang/String;)V")
    setLocalName = JavaMethod("(ILjava/lang/String;)V")
    setQName = JavaMethod("(ILjava/lang/String;)V")
    setType = JavaMethod("(ILjava/lang/String;)V")
    setValue = JavaMethod("(ILjava/lang/String;)V")