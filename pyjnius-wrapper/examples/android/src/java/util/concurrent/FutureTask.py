from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FutureTask"]

class FutureTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/FutureTask"
    __javaconstructor__ = [("(Ljava/util/concurrent/Callable;)V", False), ("(Ljava/lang/Runnable;Ljava/lang/Object;)V", False)]
    isCancelled = JavaMethod("()Z")
    isDone = JavaMethod("()Z")
    cancel = JavaMethod("(Z)Z")
    get = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    done = JavaMethod("()V")
    set = JavaMethod("(Ljava/lang/Object;)V")
    setException = JavaMethod("(Ljava/lang/Throwable;)V")
    run = JavaMethod("()V")
    runAndReset = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")