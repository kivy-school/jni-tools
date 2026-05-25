from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransferQueue"]

class TransferQueue(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/TransferQueue"
    tryTransfer = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;)Z", False, False)])
    transfer = JavaMethod("(Ljava/lang/Object;)V")
    hasWaitingConsumer = JavaMethod("()Z")
    getWaitingConsumerCount = JavaMethod("()I")