from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SeekableByteChannel"]

class SeekableByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SeekableByteChannel"
    size = JavaMethod("()J")
    position = JavaMultipleMethod([("(J)Ljava/nio/channels/SeekableByteChannel;", False, False), ("()J", False, False)])
    write = JavaMethod("(Ljava/nio/ByteBuffer;)I")
    read = JavaMethod("(Ljava/nio/ByteBuffer;)I")
    truncate = JavaMethod("(J)Ljava/nio/channels/SeekableByteChannel;")