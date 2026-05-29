from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadPoolExecutor"]

class ThreadPoolExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ThreadPoolExecutor"
    __javaconstructor__ = [("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;)V", False), ("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;Ljava/util/concurrent/ThreadFactory;)V", False), ("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;Ljava/util/concurrent/RejectedExecutionHandler;)V", False), ("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;Ljava/util/concurrent/ThreadFactory;Ljava/util/concurrent/RejectedExecutionHandler;)V", False)]
    execute = JavaMethod("(Ljava/lang/Runnable;)V")
    shutdown = JavaMethod("()V")
    shutdownNow = JavaMethod("()Ljava/util/List;")
    isShutdown = JavaMethod("()Z")
    isTerminating = JavaMethod("()Z")
    isTerminated = JavaMethod("()Z")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    finalize = JavaMethod("()V")
    setThreadFactory = JavaMethod("(Ljava/util/concurrent/ThreadFactory;)V")
    getThreadFactory = JavaMethod("()Ljava/util/concurrent/ThreadFactory;")
    setRejectedExecutionHandler = JavaMethod("(Ljava/util/concurrent/RejectedExecutionHandler;)V")
    getRejectedExecutionHandler = JavaMethod("()Ljava/util/concurrent/RejectedExecutionHandler;")
    setCorePoolSize = JavaMethod("(I)V")
    getCorePoolSize = JavaMethod("()I")
    prestartCoreThread = JavaMethod("()Z")
    prestartAllCoreThreads = JavaMethod("()I")
    allowsCoreThreadTimeOut = JavaMethod("()Z")
    allowCoreThreadTimeOut = JavaMethod("(Z)V")
    setMaximumPoolSize = JavaMethod("(I)V")
    getMaximumPoolSize = JavaMethod("()I")
    setKeepAliveTime = JavaMethod("(JLjava/util/concurrent/TimeUnit;)V")
    getKeepAliveTime = JavaMethod("(Ljava/util/concurrent/TimeUnit;)J")
    getQueue = JavaMethod("()Ljava/util/concurrent/BlockingQueue;")
    remove = JavaMethod("(Ljava/lang/Runnable;)Z")
    purge = JavaMethod("()V")
    getPoolSize = JavaMethod("()I")
    getActiveCount = JavaMethod("()I")
    getLargestPoolSize = JavaMethod("()I")
    getTaskCount = JavaMethod("()J")
    getCompletedTaskCount = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    beforeExecute = JavaMethod("(Ljava/lang/Thread;Ljava/lang/Runnable;)V")
    afterExecute = JavaMethod("(Ljava/lang/Runnable;Ljava/lang/Throwable;)V")
    terminated = JavaMethod("()V")

    class AbortPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor/AbortPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")

    class CallerRunsPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor/CallerRunsPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")

    class DiscardOldestPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor/DiscardOldestPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")

    class DiscardPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor/DiscardPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")