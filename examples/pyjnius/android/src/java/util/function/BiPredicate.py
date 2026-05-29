from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BiPredicate"]

class BiPredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BiPredicate"
    test = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    negate = JavaMethod("()Ljava/util/function/BiPredicate;")
    and = JavaMethod("(Ljava/util/function/BiPredicate;)Ljava/util/function/BiPredicate;")
    or = JavaMethod("(Ljava/util/function/BiPredicate;)Ljava/util/function/BiPredicate;")