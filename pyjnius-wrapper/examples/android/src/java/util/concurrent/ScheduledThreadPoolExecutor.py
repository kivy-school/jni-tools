from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScheduledThreadPoolExecutor"]

class ScheduledThreadPoolExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ScheduledThreadPoolExecutor"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/util/concurrent/ThreadFactory;)V", False), ("(ILjava/util/concurrent/RejectedExecutionHandler;)V", False), ("(ILjava/util/concurrent/ThreadFactory;Ljava/util/concurrent/RejectedExecutionHandler;)V", False)]
    decorateTask = JavaMultipleMethod([("(Ljava/lang/Runnable;Ljava/util/concurrent/RunnableScheduledFuture;)Ljava/util/concurrent/RunnableScheduledFuture;", False, False), ("(Ljava/util/concurrent/Callable;Ljava/util/concurrent/RunnableScheduledFuture;)Ljava/util/concurrent/RunnableScheduledFuture;", False, False)])
    schedule = JavaMultipleMethod([("(Ljava/lang/Runnable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False), ("(Ljava/util/concurrent/Callable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False)])
    scheduleAtFixedRate = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")
    scheduleWithFixedDelay = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")
    execute = JavaMethod("(Ljava/lang/Runnable;)V")
    submit = JavaMultipleMethod([("(Ljava/lang/Runnable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Future;", False, False)])
    setContinueExistingPeriodicTasksAfterShutdownPolicy = JavaMethod("(Z)V")
    getContinueExistingPeriodicTasksAfterShutdownPolicy = JavaMethod("()Z")
    setExecuteExistingDelayedTasksAfterShutdownPolicy = JavaMethod("(Z)V")
    getExecuteExistingDelayedTasksAfterShutdownPolicy = JavaMethod("()Z")
    setRemoveOnCancelPolicy = JavaMethod("(Z)V")
    getRemoveOnCancelPolicy = JavaMethod("()Z")
    shutdown = JavaMethod("()V")
    shutdownNow = JavaMethod("()Ljava/util/List;")
    getQueue = JavaMethod("()Ljava/util/concurrent/BlockingQueue;")