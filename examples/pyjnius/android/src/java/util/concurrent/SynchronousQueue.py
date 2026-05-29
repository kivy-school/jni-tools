from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SynchronousQueue"]

class SynchronousQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/SynchronousQueue"
    __javaconstructor__ = [("(Z)V", False), ("()V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    peek = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    take = JavaMethod("()Ljava/lang/Object;")
    remainingCapacity = JavaMethod("()I")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;I)I", False, False), ("(Ljava/util/Collection;)I", False, False)])
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")