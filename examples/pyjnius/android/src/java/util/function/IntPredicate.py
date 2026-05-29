from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntPredicate"]

class IntPredicate(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntPredicate"
    test = JavaMethod("(I)Z")
    and = JavaMethod("(Ljava/util/function/IntPredicate;)Ljava/util/function/IntPredicate;")
    negate = JavaMethod("()Ljava/util/function/IntPredicate;")
    or = JavaMethod("(Ljava/util/function/IntPredicate;)Ljava/util/function/IntPredicate;")