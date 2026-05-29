from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SortedSet"]

class SortedSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SortedSet"
    last = JavaMethod("()Ljava/lang/Object;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    first = JavaMethod("()Ljava/lang/Object;")
    comparator = JavaMethod("()Ljava/util/Comparator;")
    subSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedSet;")
    headSet = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedSet;")
    tailSet = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedSet;")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMultipleMethod([("()Ljava/util/SequencedSet;", False, False), ("()Ljava/util/SequencedCollection;", False, False), ("()Ljava/util/SortedSet;", False, False)])