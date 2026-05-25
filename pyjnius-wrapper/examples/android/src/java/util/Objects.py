from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Objects"]

class Objects(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Objects"
    equals = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    deepEquals = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    hashCode = JavaStaticMethod("(Ljava/lang/Object;)I")
    hash = JavaStaticMethod("([Ljava/lang/Object;)I", varargs=True)
    toString = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/String;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;)Ljava/lang/String;", True, False)])
    compare = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Comparator;)I")
    requireNonNull = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/Object;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;)Ljava/lang/Object;", True, False), ("(Ljava/lang/Object;Ljava/util/function/Supplier;)Ljava/lang/Object;", True, False)])
    isNull = JavaStaticMethod("(Ljava/lang/Object;)Z")
    nonNull = JavaStaticMethod("(Ljava/lang/Object;)Z")
    requireNonNullElse = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    requireNonNullElseGet = JavaStaticMethod("(Ljava/lang/Object;Ljava/util/function/Supplier;)Ljava/lang/Object;")
    checkIndex = JavaMultipleMethod([("(II)I", True, False), ("(JJ)J", True, False)])
    checkFromToIndex = JavaMultipleMethod([("(III)I", True, False), ("(JJJ)J", True, False)])
    checkFromIndexSize = JavaMultipleMethod([("(III)I", True, False), ("(JJJ)J", True, False)])