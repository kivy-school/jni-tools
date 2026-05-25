from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncTaskLoader"]

class AsyncTaskLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/AsyncTaskLoader"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    setUpdateThrottle = JavaMethod("(J)V")
    onForceLoad = JavaMethod("()V")
    onCancelLoad = JavaMethod("()Z")
    onCanceled = JavaMethod("(Ljava/lang/Object;)V")
    loadInBackground = JavaMethod("()Ljava/lang/Object;")
    onLoadInBackground = JavaMethod("()Ljava/lang/Object;")
    cancelLoadInBackground = JavaMethod("()V")
    isLoadInBackgroundCanceled = JavaMethod("()Z")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")