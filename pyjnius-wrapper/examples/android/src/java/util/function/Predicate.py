from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Predicate"]

class Predicate(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Predicate"
    test = JavaMethod("(Ljava/lang/Object;)Z")
    and = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")
    negate = JavaMethod("()Ljava/util/function/Predicate;")
    or = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")
    isEqual = JavaStaticMethod("(Ljava/lang/Object;)Ljava/util/function/Predicate;")
    not = JavaStaticMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")