from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReentrantLock"]

class ReentrantLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/ReentrantLock"
    __javaconstructor__ = [("()V", False), ("(Z)V", False)]
    lock = JavaMethod("()V")
    lockInterruptibly = JavaMethod("()V")
    tryLock = JavaMultipleMethod([("()Z", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    unlock = JavaMethod("()V")
    newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")
    getHoldCount = JavaMethod("()I")
    isHeldByCurrentThread = JavaMethod("()Z")
    isLocked = JavaMethod("()Z")
    isFair = JavaMethod("()Z")
    getOwner = JavaMethod("()Ljava/lang/Thread;")
    hasQueuedThreads = JavaMethod("()Z")
    hasQueuedThread = JavaMethod("(Ljava/lang/Thread;)Z")
    getQueueLength = JavaMethod("()I")
    getQueuedThreads = JavaMethod("()Ljava/util/Collection;")
    hasWaiters = JavaMethod("(Ljava/util/concurrent/locks/Condition;)Z")
    getWaitQueueLength = JavaMethod("(Ljava/util/concurrent/locks/Condition;)I")
    getWaitingThreads = JavaMethod("(Ljava/util/concurrent/locks/Condition;)Ljava/util/Collection;")
    toString = JavaMethod("()Ljava/lang/String;")