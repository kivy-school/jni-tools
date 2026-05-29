from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParsePosition"]

class ParsePosition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/ParsePosition"
    __javaconstructor__ = [("(I)V", False)]
    getErrorIndex = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    setIndex = JavaMethod("(I)V")
    setErrorIndex = JavaMethod("(I)V")
    getIndex = JavaMethod("()I")