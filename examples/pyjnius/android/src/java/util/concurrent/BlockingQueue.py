from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlockingQueue"]

class BlockingQueue(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/BlockingQueue"
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    put = JavaMethod("(Ljava/lang/Object;)V")
    take = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;")
    remainingCapacity = JavaMethod("()I")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;)I", False, False), ("(Ljava/util/Collection;I)I", False, False)])