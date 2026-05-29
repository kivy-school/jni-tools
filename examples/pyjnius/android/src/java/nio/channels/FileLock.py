from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileLock"]

class FileLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileLock"
    size = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    position = JavaMethod("()J")
    close = JavaMethod("()V")
    release = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    channel = JavaMethod("()Ljava/nio/channels/FileChannel;")
    overlaps = JavaMethod("(JJ)Z")
    acquiredBy = JavaMethod("()Ljava/nio/channels/Channel;")
    isShared = JavaMethod("()Z")