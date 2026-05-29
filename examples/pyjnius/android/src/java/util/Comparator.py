from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Comparator"]

class Comparator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Comparator"
    compare = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    reversed = JavaMethod("()Ljava/util/Comparator;")
    thenComparing = JavaMultipleMethod([("(Ljava/util/Comparator;)Ljava/util/Comparator;", False, False), ("(Ljava/util/function/Function;Ljava/util/Comparator;)Ljava/util/Comparator;", False, False), ("(Ljava/util/function/Function;)Ljava/util/Comparator;", False, False)])
    thenComparingInt = JavaMethod("(Ljava/util/function/ToIntFunction;)Ljava/util/Comparator;")
    thenComparingLong = JavaMethod("(Ljava/util/function/ToLongFunction;)Ljava/util/Comparator;")
    thenComparingDouble = JavaMethod("(Ljava/util/function/ToDoubleFunction;)Ljava/util/Comparator;")
    reverseOrder = JavaStaticMethod("()Ljava/util/Comparator;")
    naturalOrder = JavaStaticMethod("()Ljava/util/Comparator;")
    nullsFirst = JavaStaticMethod("(Ljava/util/Comparator;)Ljava/util/Comparator;")
    nullsLast = JavaStaticMethod("(Ljava/util/Comparator;)Ljava/util/Comparator;")
    comparing = JavaMultipleMethod([("(Ljava/util/function/Function;Ljava/util/Comparator;)Ljava/util/Comparator;", True, False), ("(Ljava/util/function/Function;)Ljava/util/Comparator;", True, False)])
    comparingInt = JavaStaticMethod("(Ljava/util/function/ToIntFunction;)Ljava/util/Comparator;")
    comparingLong = JavaStaticMethod("(Ljava/util/function/ToLongFunction;)Ljava/util/Comparator;")
    comparingDouble = JavaStaticMethod("(Ljava/util/function/ToDoubleFunction;)Ljava/util/Comparator;")