from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Objects"]

class Objects(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Objects"
    equals = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    toString = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/String;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;)Ljava/lang/String;", True, False)])
    checkIndex = JavaMultipleMethod([("(II)I", True, False), ("(JJ)J", True, False)])
    hashCode = JavaStaticMethod("(Ljava/lang/Object;)I")
    compare = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Comparator;)I")
    hash = JavaStaticMethod("([Ljava/lang/Object;)I", varargs=True)
    requireNonNull = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/util/function/Supplier;)Ljava/lang/Object;", True, False), ("(Ljava/lang/Object;Ljava/lang/String;)Ljava/lang/Object;", True, False), ("(Ljava/lang/Object;)Ljava/lang/Object;", True, False)])
    checkFromToIndex = JavaMultipleMethod([("(JJJ)J", True, False), ("(III)I", True, False)])
    checkFromIndexSize = JavaMultipleMethod([("(III)I", True, False), ("(JJJ)J", True, False)])
    deepEquals = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    toIdentityString = JavaStaticMethod("(Ljava/lang/Object;)Ljava/lang/String;")
    isNull = JavaStaticMethod("(Ljava/lang/Object;)Z")
    nonNull = JavaStaticMethod("(Ljava/lang/Object;)Z")
    requireNonNullElse = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    requireNonNullElseGet = JavaStaticMethod("(Ljava/lang/Object;Ljava/util/function/Supplier;)Ljava/lang/Object;")