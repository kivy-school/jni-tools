from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractQueuedLongSynchronizer"]

class AbstractQueuedLongSynchronizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/AbstractQueuedLongSynchronizer"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    release = JavaMethod("(J)Z")
    hasQueuedThreads = JavaMethod("()Z")
    isQueued = JavaMethod("(Ljava/lang/Thread;)Z")
    getQueueLength = JavaMethod("()I")
    getQueuedThreads = JavaMethod("()Ljava/util/Collection;")
    hasWaiters = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedLongSynchronizer$ConditionObject;)Z")
    getWaitQueueLength = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedLongSynchronizer$ConditionObject;)I")
    getWaitingThreads = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedLongSynchronizer$ConditionObject;)Ljava/util/Collection;")
    acquire = JavaMethod("(J)V")
    acquireInterruptibly = JavaMethod("(J)V")
    tryAcquireNanos = JavaMethod("(JJ)Z")
    getFirstQueuedThread = JavaMethod("()Ljava/lang/Thread;")
    owns = JavaMethod("(Ljava/util/concurrent/locks/AbstractQueuedLongSynchronizer$ConditionObject;)Z")
    acquireShared = JavaMethod("(J)V")
    acquireSharedInterruptibly = JavaMethod("(J)V")
    tryAcquireSharedNanos = JavaMethod("(JJ)Z")
    releaseShared = JavaMethod("(J)Z")
    hasContended = JavaMethod("()Z")
    hasQueuedPredecessors = JavaMethod("()Z")
    getExclusiveQueuedThreads = JavaMethod("()Ljava/util/Collection;")
    getSharedQueuedThreads = JavaMethod("()Ljava/util/Collection;")

    class ConditionObject(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/locks/AbstractQueuedLongSynchronizer$ConditionObject"
        __javaconstructor__ = [("(Ljava/util/concurrent/locks/AbstractQueuedLongSynchronizer;)V", False)]
        await = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()V", False, False)])
        signal = JavaMethod("()V")
        awaitUninterruptibly = JavaMethod("()V")
        awaitUntil = JavaMethod("(Ljava/util/Date;)Z")
        signalAll = JavaMethod("()V")
        awaitNanos = JavaMethod("(J)J")