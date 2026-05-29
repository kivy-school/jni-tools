from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoublePredicate"]

class DoublePredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoublePredicate"
    test = JavaMethod("(D)Z")
    negate = JavaMethod("()Ljava/util/function/DoublePredicate;")
    and = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/function/DoublePredicate;")
    or = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/function/DoublePredicate;")