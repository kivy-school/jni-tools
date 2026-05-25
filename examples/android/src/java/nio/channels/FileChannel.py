from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileChannel"]

class FileChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileChannel"
    __javaconstructor__ = [("()V", False)]
    open = JavaMultipleMethod([("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/FileChannel;", True, True), ("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/nio/channels/FileChannel;", True, True)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False), ("(Ljava/nio/ByteBuffer;J)I", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False), ("(Ljava/nio/ByteBuffer;J)I", False, False)])
    position = JavaMultipleMethod([("()J", False, False), ("(J)Ljava/nio/channels/FileChannel;", False, False)])
    size = JavaMethod("()J")
    truncate = JavaMethod("(J)Ljava/nio/channels/FileChannel;")
    force = JavaMethod("(Z)V")
    transferTo = JavaMethod("(JJLjava/nio/channels/WritableByteChannel;)J")
    transferFrom = JavaMethod("(Ljava/nio/channels/ReadableByteChannel;JJ)J")
    map = JavaMethod("(Ljava/nio/channels/FileChannel$MapMode;JJ)Ljava/nio/MappedByteBuffer;")
    lock = JavaMultipleMethod([("(JJZ)Ljava/nio/channels/FileLock;", False, False), ("()Ljava/nio/channels/FileLock;", False, False)])
    tryLock = JavaMultipleMethod([("(JJZ)Ljava/nio/channels/FileLock;", False, False), ("()Ljava/nio/channels/FileLock;", False, False)])

    class MapMode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/FileChannel/MapMode"
        PRIVATE = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        READ_ONLY = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        READ_WRITE = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        toString = JavaMethod("()Ljava/lang/String;")