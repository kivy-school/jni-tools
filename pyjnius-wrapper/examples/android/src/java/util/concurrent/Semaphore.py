from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Semaphore"]

class Semaphore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Semaphore"
    __javaconstructor__ = [("(I)V", False), ("(IZ)V", False)]
    acquire = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])
    acquireUninterruptibly = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])
    tryAcquire = JavaMultipleMethod([("()Z", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(I)Z", False, False), ("(IJLjava/util/concurrent/TimeUnit;)Z", False, False)])
    release = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])
    availablePermits = JavaMethod("()I")
    drainPermits = JavaMethod("()I")
    reducePermits = JavaMethod("(I)V")
    isFair = JavaMethod("()Z")
    hasQueuedThreads = JavaMethod("()Z")
    getQueueLength = JavaMethod("()I")
    getQueuedThreads = JavaMethod("()Ljava/util/Collection;")
    toString = JavaMethod("()Ljava/lang/String;")