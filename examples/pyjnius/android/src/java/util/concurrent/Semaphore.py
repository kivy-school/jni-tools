from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Semaphore"]

class Semaphore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Semaphore"
    __javaconstructor__ = [("(I)V", False), ("(IZ)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    release = JavaMultipleMethod([("(I)V", False, False), ("()V", False, False)])
    hasQueuedThreads = JavaMethod("()Z")
    getQueueLength = JavaMethod("()I")
    isFair = JavaMethod("()Z")
    drainPermits = JavaMethod("()I")
    acquireUninterruptibly = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])
    availablePermits = JavaMethod("()I")
    tryAcquire = JavaMultipleMethod([("(IJLjava/util/concurrent/TimeUnit;)Z", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()Z", False, False), ("(I)Z", False, False)])
    acquire = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])