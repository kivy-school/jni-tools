from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FieldPosition"]

class FieldPosition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/FieldPosition"
    __javaconstructor__ = [("(I)V", False), ("(Ljava/text/Format$Field;)V", False), ("(Ljava/text/Format$Field;I)V", False)]
    getEndIndex = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getField = JavaMethod("()I")
    getBeginIndex = JavaMethod("()I")
    getFieldAttribute = JavaMethod("()Ljava/text/Format$Field;")
    setBeginIndex = JavaMethod("(I)V")
    setEndIndex = JavaMethod("(I)V")