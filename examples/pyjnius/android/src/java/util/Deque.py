from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Deque"]

class Deque(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Deque"
    remove = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    size = JavaMethod("()I")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    peek = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMethod("()Ljava/lang/Object;")
    pollLast = JavaMethod("()Ljava/lang/Object;")
    offerLast = JavaMethod("(Ljava/lang/Object;)Z")
    peekFirst = JavaMethod("()Ljava/lang/Object;")
    removeFirstOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    offerFirst = JavaMethod("(Ljava/lang/Object;)Z")
    peekLast = JavaMethod("()Ljava/lang/Object;")
    removeLastOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    descendingIterator = JavaMethod("()Ljava/util/Iterator;")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    element = JavaMethod("()Ljava/lang/Object;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMultipleMethod([("()Ljava/util/Deque;", False, False), ("()Ljava/util/SequencedCollection;", False, False)])
    push = JavaMethod("(Ljava/lang/Object;)V")
    pop = JavaMethod("()Ljava/lang/Object;")
    pollFirst = JavaMethod("()Ljava/lang/Object;")