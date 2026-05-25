from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WritableByteChannel"]

class WritableByteChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/WritableByteChannel"
    write = JavaMethod("(Ljava/nio/ByteBuffer;)I")