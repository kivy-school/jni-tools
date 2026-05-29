from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectionKey"]

class SelectionKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/SelectionKey"
    __javaconstructor__ = [("()V", False)]
    OP_ACCEPT = JavaStaticField("I")
    OP_CONNECT = JavaStaticField("I")
    OP_READ = JavaStaticField("I")
    OP_WRITE = JavaStaticField("I")
    channel = JavaMethod("()Ljava/nio/channels/SelectableChannel;")
    selector = JavaMethod("()Ljava/nio/channels/Selector;")
    isValid = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    interestOps = JavaMultipleMethod([("()I", False, False), ("(I)Ljava/nio/channels/SelectionKey;", False, False)])
    interestOpsOr = JavaMethod("(I)I")
    interestOpsAnd = JavaMethod("(I)I")
    readyOps = JavaMethod("()I")
    isReadable = JavaMethod("()Z")
    isWritable = JavaMethod("()Z")
    isConnectable = JavaMethod("()Z")
    isAcceptable = JavaMethod("()Z")
    attach = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    attachment = JavaMethod("()Ljava/lang/Object;")