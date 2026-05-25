from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BiPredicate"]

class BiPredicate(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BiPredicate"
    test = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    and = JavaMethod("(Ljava/util/function/BiPredicate;)Ljava/util/function/BiPredicate;")
    negate = JavaMethod("()Ljava/util/function/BiPredicate;")
    or = JavaMethod("(Ljava/util/function/BiPredicate;)Ljava/util/function/BiPredicate;")