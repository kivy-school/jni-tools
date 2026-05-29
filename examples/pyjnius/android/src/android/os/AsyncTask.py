from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncTask"]

class AsyncTask(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/AsyncTask"
    __javaconstructor__ = [("()V", False)]
    SERIAL_EXECUTOR = JavaStaticField("Ljava/util/concurrent/Executor;")
    THREAD_POOL_EXECUTOR = JavaStaticField("Ljava/util/concurrent/Executor;")
    getStatus = JavaMethod("()Landroid/os/AsyncTask$Status;")
    doInBackground = JavaMethod("([Ljava/lang/Object;)Ljava/lang/Object;", varargs=True)
    onPreExecute = JavaMethod("()V")
    onPostExecute = JavaMethod("(Ljava/lang/Object;)V")
    onProgressUpdate = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    onCancelled = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("()V", False, False)])
    isCancelled = JavaMethod("()Z")
    cancel = JavaMethod("(Z)Z")
    get = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])
    execute = JavaMultipleMethod([("([Ljava/lang/Object;)Landroid/os/AsyncTask;", False, True), ("(Ljava/lang/Runnable;)V", True, False)])
    executeOnExecutor = JavaMethod("(Ljava/util/concurrent/Executor;[Ljava/lang/Object;)Landroid/os/AsyncTask;", varargs=True)
    publishProgress = JavaMethod("([Ljava/lang/Object;)V", varargs=True)

    class Status(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/AsyncTask/Status"
        values = JavaStaticMethod("()[Landroid/os/AsyncTask$Status;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/AsyncTask$Status;")
        PENDING = JavaStaticField("Landroid/os/AsyncTask/Status;")
        RUNNING = JavaStaticField("Landroid/os/AsyncTask/Status;")
        FINISHED = JavaStaticField("Landroid/os/AsyncTask/Status;")