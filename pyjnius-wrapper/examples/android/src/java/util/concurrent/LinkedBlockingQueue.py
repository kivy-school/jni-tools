from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkedBlockingQueue"]

class LinkedBlockingQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/LinkedBlockingQueue"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Ljava/util/Collection;)V", False)]
    size = JavaMethod("()I")
    remainingCapacity = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;)V")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    take = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    peek = JavaMethod("()Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;)I", False, False), ("(Ljava/util/Collection;I)I", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")