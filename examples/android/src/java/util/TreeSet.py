from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TreeSet"]

class TreeSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/TreeSet"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Comparator;)V", False), ("(Ljava/util/Collection;)V", False), ("(Ljava/util/SortedSet;)V", False)]
    iterator = JavaMethod("()Ljava/util/Iterator;")
    descendingIterator = JavaMethod("()Ljava/util/Iterator;")
    descendingSet = JavaMethod("()Ljava/util/NavigableSet;")
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    clear = JavaMethod("()V")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    subSet = JavaMultipleMethod([("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    headSet = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    tailSet = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    comparator = JavaMethod("()Ljava/util/Comparator;")
    first = JavaMethod("()Ljava/lang/Object;")
    last = JavaMethod("()Ljava/lang/Object;")
    lower = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    floor = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    ceiling = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    higher = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    pollFirst = JavaMethod("()Ljava/lang/Object;")
    pollLast = JavaMethod("()Ljava/lang/Object;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    clone = JavaMethod("()Ljava/lang/Object;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")