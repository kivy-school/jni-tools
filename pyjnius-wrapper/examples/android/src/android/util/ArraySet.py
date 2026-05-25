from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArraySet"]

class ArraySet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/ArraySet"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/util/ArraySet;)V", False), ("(Ljava/util/Collection;)V", False), ("([Ljava/lang/Object;)V", False)]
    clear = JavaMethod("()V")
    ensureCapacity = JavaMethod("(I)V")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    indexOf = JavaMethod("(Ljava/lang/Object;)I")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    isEmpty = JavaMethod("()Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    addAll = JavaMultipleMethod([("(Landroid/util/ArraySet;)V", False, False), ("(Ljava/util/Collection;)Z", False, False)])
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    removeAt = JavaMethod("(I)Ljava/lang/Object;")
    removeAll = JavaMultipleMethod([("(Landroid/util/ArraySet;)Z", False, False), ("(Ljava/util/Collection;)Z", False, False)])
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    size = JavaMethod("()I")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")