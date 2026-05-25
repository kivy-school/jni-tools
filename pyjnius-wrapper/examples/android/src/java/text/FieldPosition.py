from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FieldPosition"]

class FieldPosition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/FieldPosition"
    __javaconstructor__ = [("(I)V", False), ("(Ljava/text/Format$Field;)V", False), ("(Ljava/text/Format$Field;I)V", False)]
    getFieldAttribute = JavaMethod("()Ljava/text/Format$Field;")
    getField = JavaMethod("()I")
    getBeginIndex = JavaMethod("()I")
    getEndIndex = JavaMethod("()I")
    setBeginIndex = JavaMethod("(I)V")
    setEndIndex = JavaMethod("(I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")