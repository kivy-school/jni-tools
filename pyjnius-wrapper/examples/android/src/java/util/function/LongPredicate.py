from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongPredicate"]

class LongPredicate(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongPredicate"
    test = JavaMethod("(J)Z")
    and = JavaMethod("(Ljava/util/function/LongPredicate;)Ljava/util/function/LongPredicate;")
    negate = JavaMethod("()Ljava/util/function/LongPredicate;")
    or = JavaMethod("(Ljava/util/function/LongPredicate;)Ljava/util/function/LongPredicate;")