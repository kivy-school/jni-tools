from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Flow"]

class Flow(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Flow"
    defaultBufferSize = JavaStaticMethod("()I")

    class Processor(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow/Processor"

    class Publisher(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow/Publisher"
        subscribe = JavaMethod("(Ljava/util/concurrent/Flow$Subscriber;)V")

    class Subscriber(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow/Subscriber"
        onSubscribe = JavaMethod("(Ljava/util/concurrent/Flow$Subscription;)V")
        onNext = JavaMethod("(Ljava/lang/Object;)V")
        onError = JavaMethod("(Ljava/lang/Throwable;)V")
        onComplete = JavaMethod("()V")

    class Subscription(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow/Subscription"
        request = JavaMethod("(J)V")
        cancel = JavaMethod("()V")