from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubmissionPublisher"]

class SubmissionPublisher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/SubmissionPublisher"
    __javaconstructor__ = [("(Ljava/util/concurrent/Executor;ILjava/util/function/BiConsumer;)V", False), ("()V", False), ("(Ljava/util/concurrent/Executor;I)V", False)]
    getExecutor = JavaMethod("()Ljava/util/concurrent/Executor;")
    consume = JavaMethod("(Ljava/util/function/Consumer;)Ljava/util/concurrent/CompletableFuture;")
    close = JavaMethod("()V")
    submit = JavaMethod("(Ljava/lang/Object;)I")
    offer = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/util/function/BiPredicate;)I", False, False), ("(Ljava/lang/Object;JLjava/util/concurrent/TimeUnit;Ljava/util/function/BiPredicate;)I", False, False)])
    isClosed = JavaMethod("()Z")
    closeExceptionally = JavaMethod("(Ljava/lang/Throwable;)V")
    getClosedException = JavaMethod("()Ljava/lang/Throwable;")
    hasSubscribers = JavaMethod("()Z")
    getNumberOfSubscribers = JavaMethod("()I")
    getMaxBufferCapacity = JavaMethod("()I")
    getSubscribers = JavaMethod("()Ljava/util/List;")
    isSubscribed = JavaMethod("(Ljava/util/concurrent/Flow$Subscriber;)Z")
    estimateMinimumDemand = JavaMethod("()J")
    estimateMaximumLag = JavaMethod("()I")
    subscribe = JavaMethod("(Ljava/util/concurrent/Flow$Subscriber;)V")