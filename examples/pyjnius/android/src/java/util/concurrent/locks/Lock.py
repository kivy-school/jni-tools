from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Lock"]

class Lock(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/Lock"
    lock = JavaMethod("()V")
    lockInterruptibly = JavaMethod("()V")
    tryLock = JavaMultipleMethod([("()Z", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    unlock = JavaMethod("()V")
    newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")