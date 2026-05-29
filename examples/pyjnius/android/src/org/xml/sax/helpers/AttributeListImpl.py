from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeListImpl"]

class AttributeListImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/xml/sax/helpers/AttributeListImpl"
    __javaconstructor__ = [("()V", False), ("(Lorg/xml/sax/AttributeList;)V", False)]
    setAttributeList = JavaMethod("(Lorg/xml/sax/AttributeList;)V")
    addAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    removeAttribute = JavaMethod("(Ljava/lang/String;)V")
    clear = JavaMethod("()V")
    getLength = JavaMethod("()I")
    getName = JavaMethod("(I)Ljava/lang/String;")
    getType = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;)Ljava/lang/String;", False, False)])