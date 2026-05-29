from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncTask"]

class AsyncTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/AsyncTask"
    __javaconstructor__ = [("()V", False)]
    SERIAL_EXECUTOR = JavaStaticField("Ljava/util/concurrent/Executor;")
    THREAD_POOL_EXECUTOR = JavaStaticField("Ljava/util/concurrent/Executor;")
    getStatus = JavaMethod("()Landroid/os/AsyncTask$Status;")
    isCancelled = JavaMethod("()Z")
    executeOnExecutor = JavaMethod("(Ljava/util/concurrent/Executor;[Ljava/lang/Object;)Landroid/os/AsyncTask;", varargs=True)
    get = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False), ("()Ljava/lang/Object;", False, False)])
    cancel = JavaMethod("(Z)Z")
    execute = JavaMultipleMethod([("([Ljava/lang/Object;)Landroid/os/AsyncTask;", False, True), ("(Ljava/lang/Runnable;)V", True, False)])

    class Status(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/AsyncTask$Status"
        FINISHED = JavaStaticField("Landroid/os/AsyncTask$Status;")
        PENDING = JavaStaticField("Landroid/os/AsyncTask$Status;")
        RUNNING = JavaStaticField("Landroid/os/AsyncTask$Status;")
        values = JavaStaticMethod("()[Landroid/os/AsyncTask$Status;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/AsyncTask$Status;")
        FINISHED = JavaStaticField("Landroid/os/AsyncTask$Status;")
        PENDING = JavaStaticField("Landroid/os/AsyncTask$Status;")
        RUNNING = JavaStaticField("Landroid/os/AsyncTask$Status;")