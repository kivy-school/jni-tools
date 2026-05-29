from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectionKey"]

class SelectionKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SelectionKey"
    OP_READ = JavaStaticField("I")
    OP_WRITE = JavaStaticField("I")
    OP_CONNECT = JavaStaticField("I")
    OP_ACCEPT = JavaStaticField("I")
    isConnectable = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    attachment = JavaMethod("()Ljava/lang/Object;")
    isValid = JavaMethod("()Z")
    selector = JavaMethod("()Ljava/nio/channels/Selector;")
    isWritable = JavaMethod("()Z")
    attach = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    channel = JavaMethod("()Ljava/nio/channels/SelectableChannel;")
    isReadable = JavaMethod("()Z")
    interestOps = JavaMultipleMethod([("(I)Ljava/nio/channels/SelectionKey;", False, False), ("()I", False, False)])
    readyOps = JavaMethod("()I")
    interestOpsOr = JavaMethod("(I)I")
    interestOpsAnd = JavaMethod("(I)I")
    isAcceptable = JavaMethod("()Z")