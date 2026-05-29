from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Condition"]

class Condition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/Condition"
    await = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Z", False, False), ("()V", False, False)])
    signal = JavaMethod("()V")
    awaitUninterruptibly = JavaMethod("()V")
    awaitUntil = JavaMethod("(Ljava/util/Date;)Z")
    signalAll = JavaMethod("()V")
    awaitNanos = JavaMethod("(J)J")