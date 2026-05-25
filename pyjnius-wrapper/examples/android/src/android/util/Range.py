from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Range"]

class Range(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Range"
    __javaconstructor__ = [("(Ljava/lang/Comparable;Ljava/lang/Comparable;)V", False)]
    create = JavaStaticMethod("(Ljava/lang/Comparable;Ljava/lang/Comparable;)Landroid/util/Range;")
    getLower = JavaMethod("()Ljava/lang/Comparable;")
    getUpper = JavaMethod("()Ljava/lang/Comparable;")
    contains = JavaMultipleMethod([("(Ljava/lang/Comparable;)Z", False, False), ("(Landroid/util/Range;)Z", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    clamp = JavaMethod("(Ljava/lang/Comparable;)Ljava/lang/Comparable;")
    intersect = JavaMultipleMethod([("(Landroid/util/Range;)Landroid/util/Range;", False, False), ("(Ljava/lang/Comparable;Ljava/lang/Comparable;)Landroid/util/Range;", False, False)])
    extend = JavaMultipleMethod([("(Landroid/util/Range;)Landroid/util/Range;", False, False), ("(Ljava/lang/Comparable;Ljava/lang/Comparable;)Landroid/util/Range;", False, False), ("(Ljava/lang/Comparable;)Landroid/util/Range;", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")