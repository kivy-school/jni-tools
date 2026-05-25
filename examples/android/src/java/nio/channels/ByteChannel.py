from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteChannel"]

class ByteChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ByteChannel"