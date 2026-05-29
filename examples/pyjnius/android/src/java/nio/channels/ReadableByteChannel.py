from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadableByteChannel"]

class ReadableByteChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ReadableByteChannel"
    read = JavaMethod("(Ljava/nio/ByteBuffer;)I")