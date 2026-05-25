from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParsePosition"]

class ParsePosition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/ParsePosition"
    __javaconstructor__ = [("(I)V", False)]
    getIndex = JavaMethod("()I")
    setIndex = JavaMethod("(I)V")
    setErrorIndex = JavaMethod("(I)V")
    getErrorIndex = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")