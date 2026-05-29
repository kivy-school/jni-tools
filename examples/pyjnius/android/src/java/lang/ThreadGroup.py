from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadGroup"]

class ThreadGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ThreadGroup"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/ThreadGroup;Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getParent = JavaMethod("()Ljava/lang/ThreadGroup;")
    getMaxPriority = JavaMethod("()I")
    isDaemon = JavaMethod("()Z")
    isDestroyed = JavaMethod("()Z")
    setDaemon = JavaMethod("(Z)V")
    setMaxPriority = JavaMethod("(I)V")
    parentOf = JavaMethod("(Ljava/lang/ThreadGroup;)Z")
    checkAccess = JavaMethod("()V")
    activeCount = JavaMethod("()I")
    enumerate = JavaMultipleMethod([("([Ljava/lang/Thread;)I", False, False), ("([Ljava/lang/Thread;Z)I", False, False), ("([Ljava/lang/ThreadGroup;)I", False, False), ("([Ljava/lang/ThreadGroup;Z)I", False, False)])
    activeGroupCount = JavaMethod("()I")
    stop = JavaMethod("()V")
    interrupt = JavaMethod("()V")
    suspend = JavaMethod("()V")
    resume = JavaMethod("()V")
    destroy = JavaMethod("()V")
    list = JavaMethod("()V")
    uncaughtException = JavaMethod("(Ljava/lang/Thread;Ljava/lang/Throwable;)V")
    allowThreadSuspension = JavaMethod("(Z)Z")
    toString = JavaMethod("()Ljava/lang/String;")