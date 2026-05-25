from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DelayQueue"]

class DelayQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/DelayQueue"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False)]
    add = JavaMethod("(Ljava/util/concurrent/Delayed;)Z")
    offer = JavaMultipleMethod([("(Ljava/util/concurrent/Delayed;)Z", False, False), ("(Ljava/util/concurrent/Delayed;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    put = JavaMethod("(Ljava/util/concurrent/Delayed;)V")
    poll = JavaMultipleMethod([("()Ljava/util/concurrent/Delayed;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/Delayed;", False, False)])
    take = JavaMethod("()Ljava/util/concurrent/Delayed;")
    peek = JavaMethod("()Ljava/util/concurrent/Delayed;")
    size = JavaMethod("()I")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;)I", False, False), ("(Ljava/util/Collection;I)I", False, False)])
    clear = JavaMethod("()V")
    remainingCapacity = JavaMethod("()I")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")