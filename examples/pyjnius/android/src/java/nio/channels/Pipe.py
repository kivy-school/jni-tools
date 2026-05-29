from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pipe"]

class Pipe(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Pipe"
    __javaconstructor__ = [("()V", False)]
    source = JavaMethod("()Ljava/nio/channels/Pipe$SourceChannel;")
    sink = JavaMethod("()Ljava/nio/channels/Pipe$SinkChannel;")
    open = JavaStaticMethod("()Ljava/nio/channels/Pipe;")

    class SinkChannel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/Pipe/SinkChannel"
        __javaconstructor__ = [("(Ljava/nio/channels/spi/SelectorProvider;)V", False)]
        validOps = JavaMethod("()I")

    class SourceChannel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/channels/Pipe/SourceChannel"
        __javaconstructor__ = [("(Ljava/nio/channels/spi/SelectorProvider;)V", False)]
        validOps = JavaMethod("()I")