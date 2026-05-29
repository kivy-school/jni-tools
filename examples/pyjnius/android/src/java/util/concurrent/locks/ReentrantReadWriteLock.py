from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReentrantReadWriteLock"]

class ReentrantReadWriteLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/ReentrantReadWriteLock"
    __javaconstructor__ = [("()V", False), ("(Z)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    hasQueuedThreads = JavaMethod("()Z")
    getQueueLength = JavaMethod("()I")
    hasWaiters = JavaMethod("(Ljava/util/concurrent/locks/Condition;)Z")
    getWaitQueueLength = JavaMethod("(Ljava/util/concurrent/locks/Condition;)I")
    isFair = JavaMethod("()Z")
    hasQueuedThread = JavaMethod("(Ljava/lang/Thread;)Z")
    getReadLockCount = JavaMethod("()I")
    writeLock = JavaMultipleMethod([("()Ljava/util/concurrent/locks/ReentrantReadWriteLock$WriteLock;", False, False), ("()Ljava/util/concurrent/locks/Lock;", False, False)])
    readLock = JavaMultipleMethod([("()Ljava/util/concurrent/locks/ReentrantReadWriteLock$ReadLock;", False, False), ("()Ljava/util/concurrent/locks/Lock;", False, False)])
    isWriteLocked = JavaMethod("()Z")
    getWriteHoldCount = JavaMethod("()I")
    getReadHoldCount = JavaMethod("()I")
    isWriteLockedByCurrentThread = JavaMethod("()Z")

    class ReadLock(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/locks/ReentrantReadWriteLock$ReadLock"
        toString = JavaMethod("()Ljava/lang/String;")
        lock = JavaMethod("()V")
        lockInterruptibly = JavaMethod("()V")
        tryLock = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()Z", False, False)])
        newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")
        unlock = JavaMethod("()V")

    class WriteLock(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/locks/ReentrantReadWriteLock$WriteLock"
        toString = JavaMethod("()Ljava/lang/String;")
        lock = JavaMethod("()V")
        lockInterruptibly = JavaMethod("()V")
        tryLock = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()Z", False, False)])
        newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")
        getHoldCount = JavaMethod("()I")
        unlock = JavaMethod("()V")
        isHeldByCurrentThread = JavaMethod("()Z")