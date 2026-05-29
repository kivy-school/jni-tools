from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WritableByteChannel"]

class WritableByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/WritableByteChannel"
    write = JavaMethod("(Ljava/nio/ByteBuffer;)I")