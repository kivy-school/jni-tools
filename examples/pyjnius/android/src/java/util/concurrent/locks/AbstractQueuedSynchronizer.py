from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractQueuedSynchronizer"]

class AbstractQueuedSynchronizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/AbstractQueuedSynchronizer"
    toString = JavaMethod("()Ljava/lang/String;")
    release = JavaMethod("(I)Z")
    hasQueuedThreads = JavaMethod("()Z")
    isQueued = JavaMethod("(Ljava/lang/Thread;)Z")
    getQueueLength = JavaMethod("()I")
    getQueuedThreads = JavaMethod("()Ljava/util/Collection;")
    hasWaiters = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedSynchronizer$ConditionObject;)Z")
    getWaitQueueLength = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedSynchronizer$ConditionObject;)I")
    getWaitingThreads = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedSynchronizer$ConditionObject;)Ljava/util/Collection;")
    acquire = JavaMethod("(I)V")
    acquireInterruptibly = JavaMethod("(I)V")
    tryAcquireNanos = JavaMethod("(IJ)Z")
    getFirstQueuedThread = JavaMethod("()Ljava/lang/Thread;")
    owns = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedSynchronizer$ConditionObject;)Z")
    acquireShared = JavaMethod("(I)V")
    acquireSharedInterruptibly = JavaMethod("(I)V")
    tryAcquireSharedNanos = JavaMethod("(IJ)Z")
    releaseShared = JavaMethod("(I)Z")
    hasContended = JavaMethod("()Z")
    hasQueuedPredecessors = JavaMethod("()Z")
    getExclusiveQueuedThreads = JavaMethod("()Ljava/util/Collection;")
    getSharedQueuedThreads = JavaMethod("()Ljava/util/Collection;")

    class ConditionObject(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/locks/AbstractQueuedSynchronizer$ConditionObject"
        __javaconstructor__ = [("(Ljava/util/concurrent/locks/AbstractQueuedSynchronizer;)V", False)]
        await = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()V", False, False)])
        signal = JavaMethod("()V")
        awaitUninterruptibly = JavaMethod("()V")
        awaitUntil = JavaMethod("(Ljava/util/Date;)Z")
        signalAll = JavaMethod("()V")
        awaitNanos = JavaMethod("(J)J")