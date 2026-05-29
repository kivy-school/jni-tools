from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlockingQueue"]

class BlockingQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/BlockingQueue"
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    put = JavaMethod("(Ljava/lang/Object;)V")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    poll = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;")
    take = JavaMethod("()Ljava/lang/Object;")
    remainingCapacity = JavaMethod("()I")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;)I", False, False), ("(Ljava/util/Collection;I)I", False, False)])