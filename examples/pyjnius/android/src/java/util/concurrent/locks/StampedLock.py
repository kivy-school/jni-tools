from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StampedLock"]

class StampedLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/StampedLock"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    validate = JavaMethod("(J)Z")
    unlock = JavaMethod("(J)V")
    unlockWrite = JavaMethod("(J)V")
    unlockRead = JavaMethod("(J)V")
    getReadLockCount = JavaMethod("()I")
    writeLock = JavaMethod("()J")
    tryWriteLock = JavaMultipleMethod([("()J", False, False), ("(JLjava/util/concurrent/TimeUnit;)J", False, False)])
    writeLockInterruptibly = JavaMethod("()J")
    readLock = JavaMethod("()J")
    tryReadLock = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)J", False, False), ("()J", False, False)])
    readLockInterruptibly = JavaMethod("()J")
    tryOptimisticRead = JavaMethod("()J")
    tryConvertToWriteLock = JavaMethod("(J)J")
    tryConvertToReadLock = JavaMethod("(J)J")
    tryConvertToOptimisticRead = JavaMethod("(J)J")
    tryUnlockWrite = JavaMethod("()Z")
    tryUnlockRead = JavaMethod("()Z")
    isWriteLocked = JavaMethod("()Z")
    isReadLocked = JavaMethod("()Z")
    isWriteLockStamp = JavaStaticMethod("(J)Z")
    isReadLockStamp = JavaStaticMethod("(J)Z")
    isLockStamp = JavaStaticMethod("(J)Z")
    isOptimisticReadStamp = JavaStaticMethod("(J)Z")
    asReadLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")
    asWriteLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")
    asReadWriteLock = JavaMethod("()Ljava/util/concurrent/locks/ReadWriteLock;")