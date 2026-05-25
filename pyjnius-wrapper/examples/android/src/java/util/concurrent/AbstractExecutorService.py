from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractExecutorService"]

class AbstractExecutorService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/AbstractExecutorService"
    __javaconstructor__ = [("()V", False)]
    newTaskFor = JavaMultipleMethod([("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/RunnableFuture;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/RunnableFuture;", False, False)])
    submit = JavaMultipleMethod([("(Ljava/lang/Runnable;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/util/concurrent/Callable;)Ljava/util/concurrent/Future;", False, False)])
    invokeAny = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/lang/Object;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    invokeAll = JavaMultipleMethod([("(Ljava/util/Collection;)Ljava/util/List;", False, False), ("(Ljava/util/Collection;JLjava/util/concurrent/TimeUnit;)Ljava/util/List;", False, False)])