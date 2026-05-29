from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributeSet"]

class AttributeSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/AttributeSet"
    getAttributeBooleanValue = JavaMultipleMethod([("(IZ)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;Z)Z", False, False)])
    getAttributeFloatValue = JavaMultipleMethod([("(IF)F", False, False), ("(Ljava/lang/String;Ljava/lang/String;F)F", False, False)])
    getAttributeCount = JavaMethod("()I")
    getAttributeIntValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;I)I", False, False), ("(II)I", False, False)])
    getAttributeListValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;I)I", False, False), ("(I[Ljava/lang/String;I)I", False, False)])
    getAttributeName = JavaMethod("(I)Ljava/lang/String;")
    getAttributeNameResource = JavaMethod("(I)I")
    getAttributeNamespace = JavaMethod("(I)Ljava/lang/String;")
    getAttributeResourceValue = JavaMultipleMethod([("(II)I", False, False), ("(Ljava/lang/String;Ljava/lang/String;I)I", False, False)])
    getAttributeUnsignedIntValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;I)I", False, False), ("(II)I", False, False)])
    getAttributeValue = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", False, False)])
    getClassAttribute = JavaMethod("()Ljava/lang/String;")
    getIdAttribute = JavaMethod("()Ljava/lang/String;")
    getIdAttributeResourceValue = JavaMethod("(I)I")
    getPositionDescription = JavaMethod("()Ljava/lang/String;")
    getStyleAttribute = JavaMethod("()I")