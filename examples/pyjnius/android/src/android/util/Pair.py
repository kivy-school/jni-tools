from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pair"]

class Pair(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Pair"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/Object;)V", False)]
    first = JavaField("Ljava/lang/Object;")
    second = JavaField("Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    create = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Landroid/util/Pair;")