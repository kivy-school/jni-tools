from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SynchronousQueue"]

class SynchronousQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/SynchronousQueue"
    __javaconstructor__ = [("()V", False), ("(Z)V", False)]
    put = JavaMethod("(Ljava/lang/Object;)V")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    take = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    isEmpty = JavaMethod("()Z")
    size = JavaMethod("()I")
    remainingCapacity = JavaMethod("()I")
    clear = JavaMethod("()V")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    peek = JavaMethod("()Ljava/lang/Object;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;)I", False, False), ("(Ljava/util/Collection;I)I", False, False)])