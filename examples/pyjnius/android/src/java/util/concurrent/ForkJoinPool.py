from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ForkJoinPool"]

class ForkJoinPool(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ForkJoinPool"
    __javaconstructor__ = [("(ILjava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;Ljava/lang/Thread$UncaughtExceptionHandler;ZIIILjava/util/function/Predicate;JLjava/util/concurrent/TimeUnit;)V", False), ("()V", False), ("(I)V", False), ("(ILjava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;Ljava/lang/Thread$UncaughtExceptionHandler;Z)V", False)]
    defaultForkJoinWorkerThreadFactory = JavaStaticField("Ljava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;")
    invoke = JavaMethod("(Ljava/util/concurrent/ForkJoinTask;)Ljava/lang/Object;")
    shutdown = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    getFactory = JavaMethod("()Ljava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;")
    close = JavaMethod("()V")
    isTerminated = JavaMethod("()Z")
    getUncaughtExceptionHandler = JavaMethod("()Ljava/lang/Thread$UncaughtExceptionHandler;")
    submit = JavaMultipleMethod([("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;)Ljava/util/concurrent/ForkJoinTask;", False, False), ("(Ljava/util/concurrent/ForkJoinTask;)Ljava/util/concurrent/ForkJoinTask;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/ForkJoinTask;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/ForkJoinTask;", False, False)])
    execute = JavaMultipleMethod([("(Ljava/util/concurrent/ForkJoinTask;)V", False, False), ("(Ljava/lang/Runnable;)V", False, False)])
    externalSubmit = JavaMethod("(Ljava/util/concurrent/ForkJoinTask;)Ljava/util/concurrent/ForkJoinTask;")
    getQueuedTaskCount = JavaMethod("()J")
    lazySubmit = JavaMethod("(Ljava/util/concurrent/ForkJoinTask;)Ljava/util/concurrent/ForkJoinTask;")
    schedule = JavaMultipleMethod([("(Ljava/util/concurrent/Callable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False), ("(Ljava/lang/Runnable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False)])
    getCommonPoolParallelism = JavaStaticMethod("()I")
    isShutdown = JavaMethod("()Z")
    invokeAll = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/util/List;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/util/List;", False, False)])
    invokeAny = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/lang/Object;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    cancelDelayedTasksOnShutdown = JavaMethod("()V")
    getParallelism = JavaMethod("()I")
    commonPool = JavaStaticMethod("()Ljava/util/concurrent/ForkJoinPool;")
    setParallelism = JavaMethod("(I)I")
    invokeAllUninterruptibly = JavaMethod("(Ljava/util/Collection;)Ljava/util/List;")
    scheduleAtFixedRate = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")
    scheduleWithFixedDelay = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")
    submitWithTimeout = JavaMethod("(Ljava/util/concurrent/Callable;JLjava/util/concurrent/TimeUnit;Ljava/util/function/Consumer;)Ljava/util/concurrent/ForkJoinTask;")
    getPoolSize = JavaMethod("()I")
    getAsyncMode = JavaMethod("()Z")
    getRunningThreadCount = JavaMethod("()I")
    getActiveThreadCount = JavaMethod("()I")
    isQuiescent = JavaMethod("()Z")
    getStealCount = JavaMethod("()J")
    getQueuedSubmissionCount = JavaMethod("()I")
    getDelayedTaskCount = JavaMethod("()J")
    hasQueuedSubmissions = JavaMethod("()Z")
    shutdownNow = JavaMethod("()Ljava/util/List;")
    isTerminating = JavaMethod("()Z")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    awaitQuiescence = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    managedBlock = JavaStaticMethod("(Ljava/util/concurrent/ForkJoinPool$ManagedBlocker;)V")

    class ForkJoinWorkerThreadFactory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory"
        newThread = JavaMethod("(Ljava/util/concurrent/ForkJoinPool;)Ljava/util/concurrent/ForkJoinWorkerThread;")

    class ManagedBlocker(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ForkJoinPool$ManagedBlocker"
        isReleasable = JavaMethod("()Z")
        block = JavaMethod("()Z")