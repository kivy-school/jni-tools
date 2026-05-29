from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScheduledThreadPoolExecutor"]

class ScheduledThreadPoolExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ScheduledThreadPoolExecutor"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/util/concurrent/ThreadFactory;)V", False), ("(ILjava/util/concurrent/ThreadFactory;Ljava/util/concurrent/RejectedExecutionHandler;)V", False), ("(ILjava/util/concurrent/RejectedExecutionHandler;)V", False)]
    shutdown = JavaMethod("()V")
    getQueue = JavaMethod("()Ljava/util/concurrent/BlockingQueue;")
    submit = JavaMultipleMethod([("(Ljava/lang/Runnable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Future;", False, False)])
    execute = JavaMethod("(Ljava/lang/Runnable;)V")
    schedule = JavaMultipleMethod([("(Ljava/util/concurrent/Callable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False), ("(Ljava/lang/Runnable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False)])
    getExecuteExistingDelayedTasksAfterShutdownPolicy = JavaMethod("()Z")
    getContinueExistingPeriodicTasksAfterShutdownPolicy = JavaMethod("()Z")
    setContinueExistingPeriodicTasksAfterShutdownPolicy = JavaMethod("(Z)V")
    setExecuteExistingDelayedTasksAfterShutdownPolicy = JavaMethod("(Z)V")
    setRemoveOnCancelPolicy = JavaMethod("(Z)V")
    getRemoveOnCancelPolicy = JavaMethod("()Z")
    scheduleAtFixedRate = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")
    scheduleWithFixedDelay = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")
    shutdownNow = JavaMethod("()Ljava/util/List;")