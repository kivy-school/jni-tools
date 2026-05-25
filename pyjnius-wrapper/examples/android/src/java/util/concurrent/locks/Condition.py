from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Condition"]

class Condition(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/Condition"
    await = JavaMultipleMethod([("()V", False, False), ("(JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    awaitUninterruptibly = JavaMethod("()V")
    awaitNanos = JavaMethod("(J)J")
    awaitUntil = JavaMethod("(Ljava/util/Date;)Z")
    signal = JavaMethod("()V")
    signalAll = JavaMethod("()V")