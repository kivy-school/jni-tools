from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NavigableSet"]

class NavigableSet(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/NavigableSet"
    lower = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    floor = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    ceiling = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    higher = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    pollFirst = JavaMethod("()Ljava/lang/Object;")
    pollLast = JavaMethod("()Ljava/lang/Object;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    descendingSet = JavaMethod("()Ljava/util/NavigableSet;")
    descendingIterator = JavaMethod("()Ljava/util/Iterator;")
    subSet = JavaMultipleMethod([("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    headSet = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    tailSet = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableSet;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedSet;", False, False)])
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMethod("()Ljava/util/NavigableSet;")