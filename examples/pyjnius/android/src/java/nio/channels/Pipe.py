from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pipe"]

class Pipe(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Pipe"
    source = JavaMethod("()Ljava/nio/channels/Pipe$SourceChannel;")
    open = JavaStaticMethod("()Ljava/nio/channels/Pipe;")
    sink = JavaMethod("()Ljava/nio/channels/Pipe$SinkChannel;")

    class SinkChannel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/Pipe$SinkChannel"
        validOps = JavaMethod("()I")

    class SourceChannel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/Pipe$SourceChannel"
        validOps = JavaMethod("()I")