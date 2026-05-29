from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PriorityQueue"]

class PriorityQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PriorityQueue"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Ljava/util/Comparator;)V", False), ("(ILjava/util/Comparator;)V", False), ("(Ljava/util/Collection;)V", False), ("(Ljava/util/PriorityQueue;)V", False), ("(Ljava/util/SortedSet;)V", False)]
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    peek = JavaMethod("()Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    size = JavaMethod("()I")
    clear = JavaMethod("()V")
    poll = JavaMethod("()Ljava/lang/Object;")
    comparator = JavaMethod("()Ljava/util/Comparator;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")