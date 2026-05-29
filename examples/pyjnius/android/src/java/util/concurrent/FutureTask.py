from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FutureTask"]

class FutureTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/FutureTask"
    __javaconstructor__ = [("(Ljava/lang/Runnable;Ljava/lang/Object;)V", False), ("(Ljava/util/concurrent/Callable;)V", False)]
    isCancelled = JavaMethod("()Z")
    run = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    get = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    state = JavaMethod("()Ljava/util/concurrent/Future$State;")
    isDone = JavaMethod("()Z")
    cancel = JavaMethod("(Z)Z")
    resultNow = JavaMethod("()Ljava/lang/Object;")
    exceptionNow = JavaMethod("()Ljava/lang/Throwable;")