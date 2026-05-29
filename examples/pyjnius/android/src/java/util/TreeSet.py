from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TreeSet"]

class TreeSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/TreeSet"
    __javaconstructor__ = [("(Ljava/util/SortedSet;)V", False), ("(Ljava/util/Collection;)V", False), ("(Ljava/util/Comparator;)V", False), ("()V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    floor = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    last = JavaMethod("()Ljava/lang/Object;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    first = JavaMethod("()Ljava/lang/Object;")
    comparator = JavaMethod("()Ljava/util/Comparator;")
    pollLast = JavaMethod("()Ljava/lang/Object;")
    descendingIterator = JavaMethod("()Ljava/util/Iterator;")
    descendingSet = JavaMethod("()Ljava/util/NavigableSet;")
    ceiling = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    higher = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    subSet = JavaMultipleMethod([("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    headSet = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    tailSet = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False), ("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False)])
    lower = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    pollFirst = JavaMethod("()Ljava/lang/Object;")