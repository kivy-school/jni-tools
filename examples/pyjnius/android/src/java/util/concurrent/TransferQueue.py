from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransferQueue"]

class TransferQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/TransferQueue"
    transfer = JavaMethod("(Ljava/lang/Object;)V")
    tryTransfer = JavaMultipleMethod([("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    hasWaitingConsumer = JavaMethod("()Z")
    getWaitingConsumerCount = JavaMethod("()I")