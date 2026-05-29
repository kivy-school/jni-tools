from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConstrainedFieldPosition"]

class ConstrainedFieldPosition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/ConstrainedFieldPosition"
    __javaconstructor__ = [("()V", False)]
    getStart = JavaMethod("()I")
    constrainField = JavaMethod("(Ljava/text/Format$Field;)V")
    getInt64IterationContext = JavaMethod("()J")
    matchesField = JavaMethod("(Ljava/text/Format$Field;Ljava/lang/Object;)Z")
    getFieldValue = JavaMethod("()Ljava/lang/Object;")
    constrainClass = JavaMethod("(Ljava/lang/Class;)V")
    setInt64IterationContext = JavaMethod("(J)V")
    getLimit = JavaMethod("()I")
    reset = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    getField = JavaMethod("()Ljava/text/Format$Field;")
    setState = JavaMethod("(Ljava/text/Format$Field;Ljava/lang/Object;II)V")