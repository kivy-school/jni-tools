from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReentrantReadWriteLock"]

class ReentrantReadWriteLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/ReentrantReadWriteLock"
    __javaconstructor__ = [("()V", False), ("(Z)V", False)]
    writeLock = JavaMethod("()Ljava/util/concurrent/locks/ReentrantReadWriteLock$WriteLock;")
    readLock = JavaMethod("()Ljava/util/concurrent/locks/ReentrantReadWriteLock$ReadLock;")
    isFair = JavaMethod("()Z")
    getOwner = JavaMethod("()Ljava/lang/Thread;")
    getReadLockCount = JavaMethod("()I")
    isWriteLocked = JavaMethod("()Z")
    isWriteLockedByCurrentThread = JavaMethod("()Z")
    getWriteHoldCount = JavaMethod("()I")
    getReadHoldCount = JavaMethod("()I")
    getQueuedWriterThreads = JavaMethod("()Ljava/util/Collection;")
    getQueuedReaderThreads = JavaMethod("()Ljava/util/Collection;")
    hasQueuedThreads = JavaMethod("()Z")
    hasQueuedThread = JavaMethod("(Ljava/lang/Thread;)Z")
    getQueueLength = JavaMethod("()I")
    getQueuedThreads = JavaMethod("()Ljava/util/Collection;")
    hasWaiters = JavaMethod("(Ljava/util/concurrent/locks/Condition;)Z")
    getWaitQueueLength = JavaMethod("(Ljava/util/concurrent/locks/Condition;)I")
    getWaitingThreads = JavaMethod("(Ljava/util/concurrent/locks/Condition;)Ljava/util/Collection;")
    toString = JavaMethod("()Ljava/lang/String;")

    class ReadLock(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/locks/ReentrantReadWriteLock/ReadLock"
        __javaconstructor__ = [("(Ljava/util/concurrent/locks/ReentrantReadWriteLock;)V", False)]
        lock = JavaMethod("()V")
        lockInterruptibly = JavaMethod("()V")
        tryLock = JavaMultipleMethod([("()Z", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])
        unlock = JavaMethod("()V")
        newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")
        toString = JavaMethod("()Ljava/lang/String;")

    class WriteLock(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/locks/ReentrantReadWriteLock/WriteLock"
        __javaconstructor__ = [("(Ljava/util/concurrent/locks/ReentrantReadWriteLock;)V", False)]
        lock = JavaMethod("()V")
        lockInterruptibly = JavaMethod("()V")
        tryLock = JavaMultipleMethod([("()Z", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])
        unlock = JavaMethod("()V")
        newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")
        toString = JavaMethod("()Ljava/lang/String;")
        isHeldByCurrentThread = JavaMethod("()Z")
        getHoldCount = JavaMethod("()I")