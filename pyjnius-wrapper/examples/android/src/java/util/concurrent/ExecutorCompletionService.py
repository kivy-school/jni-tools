from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecutorCompletionService"]

class ExecutorCompletionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ExecutorCompletionService"
    __javaconstructor__ = [("(Ljava/util/concurrent/Executor;)V", False), ("(Ljava/util/concurrent/Executor;Ljava/util/concurrent/BlockingQueue;)V", False)]
    submit = JavaMultipleMethod([("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Future;", False, False)])
    take = JavaMethod("()Ljava/util/concurrent/Future;")
    poll = JavaMultipleMethod([("()Ljava/util/concurrent/Future;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/Future;", False, False)])