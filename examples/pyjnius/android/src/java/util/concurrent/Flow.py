from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Flow"]

class Flow(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Flow"
    defaultBufferSize = JavaStaticMethod("()I")

    class Processor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow$Processor"

    class Subscription(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow$Subscription"
        cancel = JavaMethod("()V")
        request = JavaMethod("(J)V")

    class Subscriber(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow$Subscriber"
        onError = JavaMethod("(Ljava/lang/Throwable;)V")
        onNext = JavaMethod("(Ljava/lang/Object;)V")
        onComplete = JavaMethod("()V")
        onSubscribe = JavaMethod("(Ljava/util/concurrent/Flow$Subscription;)V")

    class Publisher(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/concurrent/Flow$Publisher"
        subscribe = JavaMethod("(Ljava/util/concurrent/Flow$Subscriber;)V")