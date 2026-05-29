from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousByteChannel"]

class AsynchronousByteChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousByteChannel"
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False), ("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False)])