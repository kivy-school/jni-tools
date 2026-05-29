from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NavigableSet"]

class NavigableSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/NavigableSet"
    floor = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    pollLast = JavaMethod("()Ljava/lang/Object;")
    descendingIterator = JavaMethod("()Ljava/util/Iterator;")
    descendingSet = JavaMethod("()Ljava/util/NavigableSet;")
    ceiling = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    higher = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    subSet = JavaMultipleMethod([("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    headSet = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False), ("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False)])
    tailSet = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False), ("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False)])
    lower = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMultipleMethod([("()Ljava/util/SequencedSet;", False, False), ("()Ljava/util/SortedSet;", False, False), ("()Ljava/util/SequencedCollection;", False, False), ("()Ljava/util/NavigableSet;", False, False)])
    pollFirst = JavaMethod("()Ljava/lang/Object;")