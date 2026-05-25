from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayBlockingQueue"]

class ArrayBlockingQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ArrayBlockingQueue"
    __javaconstructor__ = [("(I)V", False), ("(IZ)V", False), ("(IZLjava/util/Collection;)V", False)]
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    put = JavaMethod("(Ljava/lang/Object;)V")
    poll = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    take = JavaMethod("()Ljava/lang/Object;")
    peek = JavaMethod("()Ljava/lang/Object;")
    size = JavaMethod("()I")
    remainingCapacity = JavaMethod("()I")
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