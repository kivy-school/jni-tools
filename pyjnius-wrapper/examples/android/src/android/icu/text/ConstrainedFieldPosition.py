from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConstrainedFieldPosition"]

class ConstrainedFieldPosition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/ConstrainedFieldPosition"
    __javaconstructor__ = [("()V", False)]
    reset = JavaMethod("()V")
    constrainField = JavaMethod("(Ljava/text/Format$Field;)V")
    constrainClass = JavaMethod("(Ljava/lang/Class;)V")
    getField = JavaMethod("()Ljava/text/Format$Field;")
    getStart = JavaMethod("()I")
    getLimit = JavaMethod("()I")
    getFieldValue = JavaMethod("()Ljava/lang/Object;")
    getInt64IterationContext = JavaMethod("()J")
    setInt64IterationContext = JavaMethod("(J)V")
    setState = JavaMethod("(Ljava/text/Format$Field;Ljava/lang/Object;II)V")
    matchesField = JavaMethod("(Ljava/text/Format$Field;Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")