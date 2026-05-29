from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ByteChannel"]

class ByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ByteChannel"