from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadableByteChannel"]

class ReadableByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ReadableByteChannel"
    read = JavaMethod("(Ljava/nio/ByteBuffer;)I")