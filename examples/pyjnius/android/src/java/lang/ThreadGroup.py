from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadGroup"]

class ThreadGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ThreadGroup"
    __javaconstructor__ = [("(Ljava/lang/ThreadGroup;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    interrupt = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    list = JavaMethod("()V")
    getParent = JavaMethod("()Ljava/lang/ThreadGroup;")
    setDaemon = JavaMethod("(Z)V")
    getMaxPriority = JavaMethod("()I")
    isDaemon = JavaMethod("()Z")
    activeCount = JavaMethod("()I")
    enumerate = JavaMultipleMethod([("([Ljava/lang/ThreadGroup;Z)I", False, False), ("([Ljava/lang/ThreadGroup;)I", False, False), ("([Ljava/lang/Thread;Z)I", False, False), ("([Ljava/lang/Thread;)I", False, False)])
    uncaughtException = JavaMethod("(Ljava/lang/Thread;Ljava/lang/Throwable;)V")
    checkAccess = JavaMethod("()V")
    parentOf = JavaMethod("(Ljava/lang/ThreadGroup;)Z")
    activeGroupCount = JavaMethod("()I")
    setMaxPriority = JavaMethod("(I)V")
    isDestroyed = JavaMethod("()Z")
    destroy = JavaMethod("()V")