from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ForkJoinPool"]

class ForkJoinPool(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ForkJoinPool"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(ILjava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;Ljava/lang/Thread$UncaughtExceptionHandler;Z)V", False), ("(ILjava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;Ljava/lang/Thread$UncaughtExceptionHandler;ZIIILjava/util/function/Predicate;JLjava/util/concurrent/TimeUnit;)V", False)]
    defaultForkJoinWorkerThreadFactory = JavaStaticField("Ljava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;")
    commonPool = JavaStaticMethod("()Ljava/util/concurrent/ForkJoinPool;")
    invoke = JavaMethod("(Ljava/util/concurrent/ForkJoinTask;)Ljava/lang/Object;")
    execute = JavaMultipleMethod([("(Ljava/util/concurrent/ForkJoinTask;)V", False, False), ("(Ljava/lang/Runnable;)V", False, False)])
    submit = JavaMultipleMethod([("(Ljava/util/concurrent/ForkJoinTask;)Ljava/util/concurrent/ForkJoinTask;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/ForkJoinTask;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/ForkJoinTask;", False, False), ("(Ljava/lang/Runnable;)Ljava/util/concurrent/ForkJoinTask;", False, False)])
    invokeAll = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/util/List;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/util/List;", False, False)])
    invokeAny = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/lang/Object;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    getFactory = JavaMethod("()Ljava/util/concurrent/ForkJoinPool$ForkJoinWorkerThreadFactory;")
    getUncaughtExceptionHandler = JavaMethod("()Ljava/lang/Thread$UncaughtExceptionHandler;")
    getParallelism = JavaMethod("()I")
    getCommonPoolParallelism = JavaStaticMethod("()I")
    getPoolSize = JavaMethod("()I")
    getAsyncMode = JavaMethod("()Z")
    getRunningThreadCount = JavaMethod("()I")
    getActiveThreadCount = JavaMethod("()I")
    isQuiescent = JavaMethod("()Z")
    getStealCount = JavaMethod("()J")
    getQueuedTaskCount = JavaMethod("()J")
    getQueuedSubmissionCount = JavaMethod("()I")
    hasQueuedSubmissions = JavaMethod("()Z")
    pollSubmission = JavaMethod("()Ljava/util/concurrent/ForkJoinTask;")
    drainTasksTo = JavaMethod("(Ljava/util/Collection;)I")
    toString = JavaMethod("()Ljava/lang/String;")
    shutdown = JavaMethod("()V")
    shutdownNow = JavaMethod("()Ljava/util/List;")
    isTerminated = JavaMethod("()Z")
    isTerminating = JavaMethod("()Z")
    isShutdown = JavaMethod("()Z")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    awaitQuiescence = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    managedBlock = JavaStaticMethod("(Ljava/util/concurrent/ForkJoinPool$ManagedBlocker;)V")
    newTaskFor = JavaMultipleMethod([("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/RunnableFuture;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/RunnableFuture;", False, False)])

    class ForkJoinWorkerThreadFactory(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ForkJoinPool/ForkJoinWorkerThreadFactory"
        newThread = JavaMethod("(Ljava/util/concurrent/ForkJoinPool;)Ljava/util/concurrent/ForkJoinWorkerThread;")

    class ManagedBlocker(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ForkJoinPool/ManagedBlocker"
        block = JavaMethod("()Z")
        isReleasable = JavaMethod("()Z")