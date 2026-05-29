from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecutorService"]

class ExecutorService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ExecutorService"
    shutdown = JavaMethod("()V")
    close = JavaMethod("()V")
    isTerminated = JavaMethod("()Z")
    submit = JavaMultipleMethod([("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;)Ljava/util/concurrent/Future;", False, False)])
    isShutdown = JavaMethod("()Z")
    invokeAll = JavaMultipleMethod([("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/util/List;", False, False), ("(Ljava/util/Collection;)Ljava/util/List;", False, False)])
    invokeAny = JavaMultipleMethod([("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("(Ljava/util/Collection;)Ljava/lang/Object;", False, False)])
    shutdownNow = JavaMethod("()Ljava/util/List;")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")