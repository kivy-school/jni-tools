from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeListImpl"]

class AttributeListImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/AttributeListImpl"
    __javaconstructor__ = [("(Lorg/xml/sax/AttributeList;)V", False), ("()V", False)]
    removeAttribute = JavaMethod("(Ljava/lang/String;)V")
    getName = JavaMethod("(I)Ljava/lang/String;")
    getLength = JavaMethod("()I")
    clear = JavaMethod("()V")
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getType = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    setAttributeList = JavaMethod("(Lorg/xml/sax/AttributeList;)V")
    addAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")