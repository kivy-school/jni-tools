from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsyncTaskLoader"]

class AsyncTaskLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/AsyncTaskLoader"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    loadInBackground = JavaMethod("()Ljava/lang/Object;")
    cancelLoadInBackground = JavaMethod("()V")
    isLoadInBackgroundCanceled = JavaMethod("()Z")
    onCanceled = JavaMethod("(Ljava/lang/Object;)V")
    setUpdateThrottle = JavaMethod("(J)V")