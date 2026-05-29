from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkedTransferQueue"]

class LinkedTransferQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/LinkedTransferQueue"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    put = JavaMethod("(Ljava/lang/Object;)V")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    add = JavaMethod("(Ljava/lang/Object;)Z")
    tryTransfer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    transfer = JavaMethod("(Ljava/lang/Object;)V")
    take = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;)I", False, False), ("(Ljava/util/Collection;I)I", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    peek = JavaMethod("()Ljava/lang/Object;")
    isEmpty = JavaMethod("()Z")
    hasWaitingConsumer = JavaMethod("()Z")
    size = JavaMethod("()I")
    getWaitingConsumerCount = JavaMethod("()I")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    remainingCapacity = JavaMethod("()I")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    clear = JavaMethod("()V")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")