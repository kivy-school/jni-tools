from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Future"]

class Future(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Future"
    isCancelled = JavaMethod("()Z")
    get = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    state = JavaMethod("()Ljava/util/concurrent/Future$State;")
    isDone = JavaMethod("()Z")
    cancel = JavaMethod("(Z)Z")
    resultNow = JavaMethod("()Ljava/lang/Object;")
    exceptionNow = JavaMethod("()Ljava/lang/Throwable;")

    class State(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Future$State"
        RUNNING = JavaStaticField("Ljava/util/concurrent/Future$State;")
        SUCCESS = JavaStaticField("Ljava/util/concurrent/Future$State;")
        FAILED = JavaStaticField("Ljava/util/concurrent/Future$State;")
        CANCELLED = JavaStaticField("Ljava/util/concurrent/Future$State;")
        values = JavaStaticMethod("()[Ljava/util/concurrent/Future$State;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/concurrent/Future$State;")
        RUNNING = JavaStaticField("Ljava/util/concurrent/Future$State;")
        SUCCESS = JavaStaticField("Ljava/util/concurrent/Future$State;")
        FAILED = JavaStaticField("Ljava/util/concurrent/Future$State;")
        CANCELLED = JavaStaticField("Ljava/util/concurrent/Future$State;")