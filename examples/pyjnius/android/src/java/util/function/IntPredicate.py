from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntPredicate"]

class IntPredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntPredicate"
    test = JavaMethod("(I)Z")
    negate = JavaMethod("()Ljava/util/function/IntPredicate;")
    and = JavaMethod("(Ljava/util/function/IntPredicate;)Ljava/util/function/IntPredicate;")
    or = JavaMethod("(Ljava/util/function/IntPredicate;)Ljava/util/function/IntPredicate;")