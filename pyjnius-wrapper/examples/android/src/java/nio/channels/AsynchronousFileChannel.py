from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousFileChannel"]

class AsynchronousFileChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousFileChannel"
    __javaconstructor__ = [("()V", False)]
    open = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Set;Ljava/util/concurrent/ExecutorService;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/AsynchronousFileChannel;", True, True), ("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/nio/channels/AsynchronousFileChannel;", True, True)])
    size = JavaMethod("()J")
    truncate = JavaMethod("(J)Ljava/nio/channels/AsynchronousFileChannel;")
    force = JavaMethod("(Z)V")
    lock = JavaMultipleMethod([("(JJZLjava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(JJZ)Ljava/util/concurrent/Future;", False, False), ("()Ljava/util/concurrent/Future;", False, False)])
    tryLock = JavaMultipleMethod([("(JJZ)Ljava/nio/channels/FileLock;", False, False), ("()Ljava/nio/channels/FileLock;", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;J)Ljava/util/concurrent/Future;", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;JLjava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;J)Ljava/util/concurrent/Future;", False, False)])