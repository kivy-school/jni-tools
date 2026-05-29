from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PriorityQueue"]

class PriorityQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PriorityQueue"
    __javaconstructor__ = [("(ILjava/util/Comparator;)V", False), ("(Ljava/util/Collection;)V", False), ("(Ljava/util/PriorityQueue;)V", False), ("(Ljava/util/SortedSet;)V", False), ("()V", False), ("(I)V", False), ("(Ljava/util/Comparator;)V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    clear = JavaMethod("()V")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False), ("()[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    peek = JavaMethod("()Ljava/lang/Object;")
    comparator = JavaMethod("()Ljava/util/Comparator;")
    poll = JavaMethod("()Ljava/lang/Object;")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")