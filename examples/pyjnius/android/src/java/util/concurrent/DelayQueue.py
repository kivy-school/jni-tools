from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DelayQueue"]

class DelayQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/DelayQueue"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False)]
    remove = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("()Ljava/util/concurrent/Delayed;", False, False), ("()Ljava/lang/Object;", False, False)])
    size = JavaMethod("()I")
    put = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/util/concurrent/Delayed;)V", False, False)])
    clear = JavaMethod("()V")
    add = JavaMultipleMethod([("(Ljava/util/concurrent/Delayed;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    toArray = JavaMultipleMethod([("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False), ("()[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    offer = JavaMultipleMethod([("(Ljava/util/concurrent/Delayed;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False), ("(Ljava/util/concurrent/Delayed;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    peek = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Ljava/util/concurrent/Delayed;", False, False)])
    poll = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Ljava/util/concurrent/Delayed;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/Delayed;", False, False)])
    take = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Ljava/util/concurrent/Delayed;", False, False)])
    remainingCapacity = JavaMethod("()I")
    drainTo = JavaMultipleMethod([("(Ljava/util/Collection;I)I", False, False), ("(Ljava/util/Collection;)I", False, False)])