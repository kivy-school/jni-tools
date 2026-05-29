from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayBlockingQueue"]

class ArrayBlockingQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ArrayBlockingQueue"
    __javaconstructor__ = [("(IZLjava/util/Collection;)V", False), ("(I)V", False), ("(IZ)V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    peek = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    take = JavaMethod("()Ljava/lang/Object;")
    remainingCapacity = JavaMethod("()I")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;I)I", False, False), ("(Ljava/util/Collection;)I", False, False)])
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")