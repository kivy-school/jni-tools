from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousByteChannel"]

class AsynchronousByteChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousByteChannel"
    read = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False)])
    write = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;Ljava/lang/Object;Ljava/nio/channels/CompletionHandler;)V", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/concurrent/Future;", False, False)])