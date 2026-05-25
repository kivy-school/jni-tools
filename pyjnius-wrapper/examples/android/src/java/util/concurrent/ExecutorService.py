from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecutorService"]

class ExecutorService(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ExecutorService"
    shutdown = JavaMethod("()V")
    shutdownNow = JavaMethod("()Ljava/util/List;")
    isShutdown = JavaMethod("()Z")
    isTerminated = JavaMethod("()Z")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    submit = JavaMultipleMethod([("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;)Ljava/util/concurrent/Future;", False, False)])
    invokeAll = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/util/List;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/util/List;", False, False)])
    invokeAny = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/lang/Object;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])