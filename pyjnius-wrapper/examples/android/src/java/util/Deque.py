from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Deque"]

class Deque(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Deque"
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    offerFirst = JavaMethod("(Ljava/lang/Object;)Z")
    offerLast = JavaMethod("(Ljava/lang/Object;)Z")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    pollFirst = JavaMethod("()Ljava/lang/Object;")
    pollLast = JavaMethod("()Ljava/lang/Object;")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    peekFirst = JavaMethod("()Ljava/lang/Object;")
    peekLast = JavaMethod("()Ljava/lang/Object;")
    removeFirstOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    removeLastOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    poll = JavaMethod("()Ljava/lang/Object;")
    element = JavaMethod("()Ljava/lang/Object;")
    peek = JavaMethod("()Ljava/lang/Object;")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    push = JavaMethod("(Ljava/lang/Object;)V")
    pop = JavaMethod("()Ljava/lang/Object;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    descendingIterator = JavaMethod("()Ljava/util/Iterator;")
    reversed = JavaMethod("()Ljava/util/Deque;")