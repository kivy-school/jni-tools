from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Range"]

class Range(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Range"
    __javaconstructor__ = [("(Ljava/lang/Comparable;Ljava/lang/Comparable;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clamp = JavaMethod("(Ljava/lang/Comparable;)Ljava/lang/Comparable;")
    contains = JavaMultipleMethod([("(Ljava/lang/Comparable;)Z", False, False), ("(Landroid/util/Range;)Z", False, False)])
    create = JavaStaticMethod("(Ljava/lang/Comparable;Ljava/lang/Comparable;)Landroid/util/Range;")
    extend = JavaMultipleMethod([("(Ljava/lang/Comparable;)Landroid/util/Range;", False, False), ("(Landroid/util/Range;)Landroid/util/Range;", False, False), ("(Ljava/lang/Comparable;Ljava/lang/Comparable;)Landroid/util/Range;", False, False)])
    intersect = JavaMultipleMethod([("(Ljava/lang/Comparable;Ljava/lang/Comparable;)Landroid/util/Range;", False, False), ("(Landroid/util/Range;)Landroid/util/Range;", False, False)])
    getUpper = JavaMethod("()Ljava/lang/Comparable;")
    getLower = JavaMethod("()Ljava/lang/Comparable;")