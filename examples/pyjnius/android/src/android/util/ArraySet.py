from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArraySet"]

class ArraySet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/ArraySet"
    __javaconstructor__ = [("(Ljava/util/Collection;)V", False), ("(I)V", False), ("([Ljava/lang/Object;)V", False), ("(Landroid/util/ArraySet;)V", False), ("()V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    indexOf = JavaMethod("(Ljava/lang/Object;)I")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    addAll = JavaMultipleMethod([("(Ljava/util/Collection;)Z", False, False), ("(Landroid/util/ArraySet;)V", False, False)])
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    ensureCapacity = JavaMethod("(I)V")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    removeAt = JavaMethod("(I)Ljava/lang/Object;")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMultipleMethod([("(Landroid/util/ArraySet;)Z", False, False), ("(Ljava/util/Collection;)Z", False, False)])
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")