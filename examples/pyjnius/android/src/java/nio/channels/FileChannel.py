from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileChannel"]

class FileChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileChannel"
    size = JavaMethod("()J")
    position = JavaMultipleMethod([("(J)Ljava/nio/channels/FileChannel;", False, False), ("()J", False, False), ("(J)Ljava/nio/channels/SeekableByteChannel;", False, False)])
    map = JavaMultipleMethod([("(Ljava/nio/channels/FileChannel$MapMode;JJ)Ljava/nio/MappedByteBuffer;", False, False), ("(Ljava/nio/channels/FileChannel$MapMode;JJLjava/lang/foreign/Arena;)Ljava/lang/foreign/MemorySegment;", False, False)])
    lock = JavaMultipleMethod([("(JJZ)Ljava/nio/channels/FileLock;", False, False), ("()Ljava/nio/channels/FileLock;", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;J)I", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("(Ljava/nio/ByteBuffer;)I", False, False)])
    open = JavaMultipleMethod([("(Ljava/nio/file/Path;[Ljava/nio/file/OpenOption;)Ljava/nio/channels/FileChannel;", True, True), ("(Ljava/nio/file/Path;Ljava/util/Set;[Ljava/nio/file/attribute/FileAttribute;)Ljava/nio/channels/FileChannel;", True, True)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)I", False, False), ("([Ljava/nio/ByteBuffer;II)J", False, False), ("(Ljava/nio/ByteBuffer;J)I", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])
    transferTo = JavaMethod("(JJLjava/nio/channels/WritableByteChannel;)J")
    force = JavaMethod("(Z)V")
    tryLock = JavaMultipleMethod([("()Ljava/nio/channels/FileLock;", False, False), ("(JJZ)Ljava/nio/channels/FileLock;", False, False)])
    truncate = JavaMultipleMethod([("(J)Ljava/nio/channels/FileChannel;", False, False), ("(J)Ljava/nio/channels/SeekableByteChannel;", False, False)])
    transferFrom = JavaMethod("(Ljava/nio/channels/ReadableByteChannel;JJ)J")

    class MapMode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/FileChannel$MapMode"
        READ_ONLY = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        READ_WRITE = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        PRIVATE = JavaStaticField("Ljava/nio/channels/FileChannel$MapMode;")
        toString = JavaMethod("()Ljava/lang/String;")