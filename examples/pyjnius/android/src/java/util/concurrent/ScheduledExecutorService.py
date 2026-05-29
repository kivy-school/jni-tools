from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScheduledExecutorService"]

class ScheduledExecutorService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ScheduledExecutorService"
    schedule = JavaMultipleMethod([("(Ljava/lang/Runnable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False), ("(Ljava/util/concurrent/Callable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;", False, False)])
    scheduleAtFixedRate = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")
    scheduleWithFixedDelay = JavaMethod("(Ljava/lang/Runnable;JJLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;")