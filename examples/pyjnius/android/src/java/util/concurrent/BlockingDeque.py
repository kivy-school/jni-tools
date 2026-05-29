from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlockingDeque"]

class BlockingDeque(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/BlockingDeque"
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    offerFirst = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    offerLast = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    putFirst = JavaMethod("(Ljava/lang/Object;)V")
    putLast = JavaMethod("(Ljava/lang/Object;)V")
    takeFirst = JavaMethod("()Ljava/lang/Object;")
    takeLast = JavaMethod("()Ljava/lang/Object;")
    pollFirst = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;")
    pollLast = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;")
    removeFirstOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    removeLastOccurrence = JavaMethod("(Ljava/lang/Object;)Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    put = JavaMethod("(Ljava/lang/Object;)V")
    remove = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    poll = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    take = JavaMethod("()Ljava/lang/Object;")
    element = JavaMethod("()Ljava/lang/Object;")
    peek = JavaMethod("()Ljava/lang/Object;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    push = JavaMethod("(Ljava/lang/Object;)V")