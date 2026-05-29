from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SeekableByteChannel"]

class SeekableByteChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SeekableByteChannel"
    read = JavaMethod("(Ljava/nio/ByteBuffer;)I")
    write = JavaMethod("(Ljava/nio/ByteBuffer;)I")
    position = JavaMultipleMethod([("()J", False, False), ("(J)Ljava/nio/channels/SeekableByteChannel;", False, False)])
    size = JavaMethod("()J")
    truncate = JavaMethod("(J)Ljava/nio/channels/SeekableByteChannel;")