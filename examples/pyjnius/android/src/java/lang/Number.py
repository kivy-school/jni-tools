from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Number"]

class Number(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Number"
    __javaconstructor__ = [("()V", False)]
    intValue = JavaMethod("()I")
    longValue = JavaMethod("()J")
    floatValue = JavaMethod("()F")
    doubleValue = JavaMethod("()D")
    byteValue = JavaMethod("()B")
    shortValue = JavaMethod("()S")