from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeSet"]

class AttributeSet(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/AttributeSet"
    getAttributeCount = JavaMethod("()I")
    getAttributeNamespace = JavaMethod("(I)Ljava/lang/String;")
    getAttributeName = JavaMethod("(I)Ljava/lang/String;")
    getAttributeValue = JavaMultipleMethod([("(I)Ljava/lang/String;", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getPositionDescription = JavaMethod("()Ljava/lang/String;")
    getAttributeNameResource = JavaMethod("(I)I")
    getAttributeListValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;I)I", False, False), ("(I[Ljava/lang/String;I)I", False, False)])
    getAttributeBooleanValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Z)Z", False, False), ("(IZ)Z", False, False)])
    getAttributeResourceValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;I)I", False, False), ("(II)I", False, False)])
    getAttributeIntValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;I)I", False, False), ("(II)I", False, False)])
    getAttributeUnsignedIntValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;I)I", False, False), ("(II)I", False, False)])
    getAttributeFloatValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;F)F", False, False), ("(IF)F", False, False)])
    getIdAttribute = JavaMethod("()Ljava/lang/String;")
    getClassAttribute = JavaMethod("()Ljava/lang/String;")
    getIdAttributeResourceValue = JavaMethod("(I)I")
    getStyleAttribute = JavaMethod("()I")