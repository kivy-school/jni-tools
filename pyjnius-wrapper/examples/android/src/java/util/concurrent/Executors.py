from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Executors"]

class Executors(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Executors"
    newFixedThreadPool = JavaMultipleMethod([("(I)Ljava/util/concurrent/ExecutorService;", True, False), ("(ILjava/util/concurrent/ThreadFactory;)Ljava/util/concurrent/ExecutorService;", True, False)])
    newWorkStealingPool = JavaMultipleMethod([("(I)Ljava/util/concurrent/ExecutorService;", True, False), ("()Ljava/util/concurrent/ExecutorService;", True, False)])
    newSingleThreadExecutor = JavaMultipleMethod([("()Ljava/util/concurrent/ExecutorService;", True, False), ("(Ljava/util/concurrent/ThreadFactory;)Ljava/util/concurrent/ExecutorService;", True, False)])
    newCachedThreadPool = JavaMultipleMethod([("()Ljava/util/concurrent/ExecutorService;", True, False), ("(Ljava/util/concurrent/ThreadFactory;)Ljava/util/concurrent/ExecutorService;", True, False)])
    newSingleThreadScheduledExecutor = JavaMultipleMethod([("()Ljava/util/concurrent/ScheduledExecutorService;", True, False), ("(Ljava/util/concurrent/ThreadFactory;)Ljava/util/concurrent/ScheduledExecutorService;", True, False)])
    newScheduledThreadPool = JavaMultipleMethod([("(I)Ljava/util/concurrent/ScheduledExecutorService;", True, False), ("(ILjava/util/concurrent/ThreadFactory;)Ljava/util/concurrent/ScheduledExecutorService;", True, False)])
    unconfigurableExecutorService = JavaStaticMethod("(Ljava/util/concurrent/ExecutorService;)Ljava/util/concurrent/ExecutorService;")
    unconfigurableScheduledExecutorService = JavaStaticMethod("(Ljava/util/concurrent/ScheduledExecutorService;)Ljava/util/concurrent/ScheduledExecutorService;")
    defaultThreadFactory = JavaStaticMethod("()Ljava/util/concurrent/ThreadFactory;")
    privilegedThreadFactory = JavaStaticMethod("()Ljava/util/concurrent/ThreadFactory;")
    callable = JavaMultipleMethod([("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Callable;", True, False), ("(Ljava/lang/Runnable;)Ljava/util/concurrent/Callable;", True, False), ("(Ljava/security/PrivilegedAction;)Ljava/util/concurrent/Callable;", True, False), ("(Ljava/security/PrivilegedExceptionAction;)Ljava/util/concurrent/Callable;", True, False)])
    privilegedCallable = JavaStaticMethod("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Callable;")
    privilegedCallableUsingCurrentClassLoader = JavaStaticMethod("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Callable;")