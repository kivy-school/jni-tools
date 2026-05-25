from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Enum"]

class Enum(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Enum"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
    name = JavaMethod("()Ljava/lang/String;")
    ordinal = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    compareTo = JavaMethod("(Ljava/lang/Enum;)I")
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    valueOf = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Enum;")
    finalize = JavaMethod("()V")