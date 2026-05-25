from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pair"]

class Pair(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Pair"
    __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/Object;)V", False)]
    first = JavaField("Ljava/lang/Object;")
    second = JavaField("Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    create = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Landroid/util/Pair;")