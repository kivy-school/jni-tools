from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Predicate"]

class Predicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Predicate"
    test = JavaMethod("(Ljava/lang/Object;)Z")
    negate = JavaMethod("()Ljava/util/function/Predicate;")
    isEqual = JavaStaticMethod("(Ljava/lang/Object;)Ljava/util/function/Predicate;")
    not = JavaStaticMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")
    and = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")
    or = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")