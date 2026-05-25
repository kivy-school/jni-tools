from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StampedLock"]

class StampedLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/StampedLock"
    __javaconstructor__ = [("()V", False)]
    writeLock = JavaMethod("()J")
    tryWriteLock = JavaMultipleMethod([("()J", False, False), ("(JLjava/util/concurrent/TimeUnit;)J", False, False)])
    writeLockInterruptibly = JavaMethod("()J")
    readLock = JavaMethod("()J")
    tryReadLock = JavaMultipleMethod([("()J", False, False), ("(JLjava/util/concurrent/TimeUnit;)J", False, False)])
    readLockInterruptibly = JavaMethod("()J")
    tryOptimisticRead = JavaMethod("()J")
    validate = JavaMethod("(J)Z")
    unlockWrite = JavaMethod("(J)V")
    unlockRead = JavaMethod("(J)V")
    unlock = JavaMethod("(J)V")
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
    getReadLockCount = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    asReadLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")
    asWriteLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")
    asReadWriteLock = JavaMethod("()Ljava/util/concurrent/locks/ReadWriteLock;")