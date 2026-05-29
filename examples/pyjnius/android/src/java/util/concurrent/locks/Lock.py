from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Lock"]

class Lock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/Lock"
    lock = JavaMethod("()V")
    lockInterruptibly = JavaMethod("()V")
    tryLock = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()Z", False, False)])
    newCondition = JavaMethod("()Ljava/util/concurrent/locks/Condition;")
    unlock = JavaMethod("()V")