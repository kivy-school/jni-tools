from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReentrantLock"]

class ReentrantLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/ReentrantLock"
    __javaconstructor__ = [("()V", False), ("(Z)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    lock = JavaMethod("()V")
    lockInterruptibly = JavaMethod("()V")
    tryLock = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()Z", False, False)])
    newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")
    getHoldCount = JavaMethod("()I")
    isLocked = JavaMethod("()Z")
    hasQueuedThreads = JavaMethod("()Z")
    getQueueLength = JavaMethod("()I")
    hasWaiters = JavaMethod("(Ljava/util/concurrent/locks/Condition;)Z")
    getWaitQueueLength = JavaMethod("(Ljava/util/concurrent/locks/Condition;)I")
    unlock = JavaMethod("()V")
    isHeldByCurrentThread = JavaMethod("()Z")
    isFair = JavaMethod("()Z")
    hasQueuedThread = JavaMethod("(Ljava/lang/Thread;)Z")