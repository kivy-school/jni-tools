from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlockingDeque"]

class BlockingDeque(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/BlockingDeque"
    remove = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("()Ljava/lang/Object;", False, False)])
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;)V")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    peek = JavaMethod("()Ljava/lang/Object;")
    putFirst = JavaMethod("(Ljava/lang/Object;)V")
    putLast = JavaMethod("(Ljava/lang/Object;)V")
    poll = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    takeFirst = JavaMethod("()Ljava/lang/Object;")
    takeLast = JavaMethod("()Ljava/lang/Object;")
    take = JavaMethod("()Ljava/lang/Object;")
    pollLast = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;")
    offerLast = JavaMultipleMethod([("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    removeFirstOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    offerFirst = JavaMultipleMethod([("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    removeLastOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    element = JavaMethod("()Ljava/lang/Object;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    push = JavaMethod("(Ljava/lang/Object;)V")
    pollFirst = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;")