from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileLock"]

class FileLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileLock"
    __javaconstructor__ = [("(Ljava/nio/channels/FileChannel;JJZ)V", False), ("(Ljava/nio/channels/AsynchronousFileChannel;JJZ)V", False)]
    channel = JavaMethod("()Ljava/nio/channels/FileChannel;")
    acquiredBy = JavaMethod("()Ljava/nio/channels/Channel;")
    position = JavaMethod("()J")
    size = JavaMethod("()J")
    isShared = JavaMethod("()Z")
    overlaps = JavaMethod("(JJ)Z")
    isValid = JavaMethod("()Z")
    release = JavaMethod("()V")
    close = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")