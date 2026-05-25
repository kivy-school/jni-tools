from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScatteringByteChannel"]

class ScatteringByteChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ScatteringByteChannel"
    read = JavaMultipleMethod([("([Ljava/nio/ByteBuffer;II)J", False, False), ("([Ljava/nio/ByteBuffer;)J", False, False)])