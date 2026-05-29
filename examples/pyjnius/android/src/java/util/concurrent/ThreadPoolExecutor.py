from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadPoolExecutor"]

class ThreadPoolExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ThreadPoolExecutor"
    __javaconstructor__ = [("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;Ljava/util/concurrent/ThreadFactory;)V", False), ("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;)V", False), ("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;Ljava/util/concurrent/RejectedExecutionHandler;)V", False), ("(IIJLjava/util/concurrent/TimeUnit;Ljava/util/concurrent/BlockingQueue;Ljava/util/concurrent/ThreadFactory;Ljava/util/concurrent/RejectedExecutionHandler;)V", False)]
    remove = JavaMethod("(Ljava/lang/Runnable;)Z")
    shutdown = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    getQueue = JavaMethod("()Ljava/util/concurrent/BlockingQueue;")
    isTerminated = JavaMethod("()Z")
    execute = JavaMethod("(Ljava/lang/Runnable;)V")
    isShutdown = JavaMethod("()Z")
    getPoolSize = JavaMethod("()I")
    shutdownNow = JavaMethod("()Ljava/util/List;")
    isTerminating = JavaMethod("()Z")
    awaitTermination = JavaMethod("(JLjava/util/concurrent/TimeUnit;)Z")
    setThreadFactory = JavaMethod("(Ljava/util/concurrent/ThreadFactory;)V")
    getThreadFactory = JavaMethod("()Ljava/util/concurrent/ThreadFactory;")
    setRejectedExecutionHandler = JavaMethod("(Ljava/util/concurrent/RejectedExecutionHandler;)V")
    getRejectedExecutionHandler = JavaMethod("()Ljava/util/concurrent/RejectedExecutionHandler;")
    setCorePoolSize = JavaMethod("(I)V")
    getCorePoolSize = JavaMethod("()I")
    prestartCoreThread = JavaMethod("()Z")
    prestartAllCoreThreads = JavaMethod("()I")
    setMaximumPoolSize = JavaMethod("(I)V")
    getMaximumPoolSize = JavaMethod("()I")
    setKeepAliveTime = JavaMethod("(JLjava/util/concurrent/TimeUnit;)V")
    getKeepAliveTime = JavaMethod("(Ljava/util/concurrent/TimeUnit;)J")
    purge = JavaMethod("()V")
    getActiveCount = JavaMethod("()I")
    getLargestPoolSize = JavaMethod("()I")
    getTaskCount = JavaMethod("()J")
    getCompletedTaskCount = JavaMethod("()J")
    allowCoreThreadTimeOut = JavaMethod("(Z)V")
    allowsCoreThreadTimeOut = JavaMethod("()Z")

    class AbortPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor$AbortPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")

    class DiscardOldestPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor$DiscardOldestPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")

    class DiscardPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor$DiscardPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")

    class CallerRunsPolicy(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/ThreadPoolExecutor$CallerRunsPolicy"
        __javaconstructor__ = [("()V", False)]
        rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")