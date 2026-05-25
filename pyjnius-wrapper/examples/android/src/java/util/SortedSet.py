from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SortedSet"]

class SortedSet(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SortedSet"
    comparator = JavaMethod("()Ljava/util/Comparator;")
    subSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedSet;")
    headSet = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedSet;")
    tailSet = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedSet;")
    first = JavaMethod("()Ljava/lang/Object;")
    last = JavaMethod("()Ljava/lang/Object;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMethod("()Ljava/util/SortedSet;")