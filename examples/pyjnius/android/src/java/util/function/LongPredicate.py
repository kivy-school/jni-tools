from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongPredicate"]

class LongPredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongPredicate"
    test = JavaMethod("(J)Z")
    negate = JavaMethod("()Ljava/util/function/LongPredicate;")
    and = JavaMethod("(Ljava/util/function/LongPredicate;)Ljava/util/function/LongPredicate;")
    or = JavaMethod("(Ljava/util/function/LongPredicate;)Ljava/util/function/LongPredicate;")