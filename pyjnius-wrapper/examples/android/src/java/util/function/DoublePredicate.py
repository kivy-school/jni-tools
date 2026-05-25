from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoublePredicate"]

class DoublePredicate(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoublePredicate"
    test = JavaMethod("(D)Z")
    and = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/function/DoublePredicate;")
    negate = JavaMethod("()Ljava/util/function/DoublePredicate;")
    or = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/function/DoublePredicate;")