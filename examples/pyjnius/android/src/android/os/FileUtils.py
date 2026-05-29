from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileUtils"]

class FileUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/FileUtils"
    copy = JavaMultipleMethod([("(Ljava/io/FileDescriptor;Ljava/io/FileDescriptor;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/FileUtils$ProgressListener;)J", True, False), ("(Ljava/io/InputStream;Ljava/io/OutputStream;)J", True, False), ("(Ljava/io/InputStream;Ljava/io/OutputStream;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/FileUtils$ProgressListener;)J", True, False), ("(Ljava/io/FileDescriptor;Ljava/io/FileDescriptor;)J", True, False)])
    closeQuietly = JavaMultipleMethod([("(Ljava/lang/AutoCloseable;)V", True, False), ("(Ljava/io/FileDescriptor;)V", True, False)])

    class ProgressListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/FileUtils$ProgressListener"
        onProgress = JavaMethod("(J)V")