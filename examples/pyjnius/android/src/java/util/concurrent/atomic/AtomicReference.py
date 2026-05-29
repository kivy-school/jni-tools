from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicReference"]

class AtomicReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicReference"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False), ("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    get = JavaMethod("()Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;)V")
    getOpaque = JavaMethod("()Ljava/lang/Object;")
    setOpaque = JavaMethod("(Ljava/lang/Object;)V")
    getAcquire = JavaMethod("()Ljava/lang/Object;")
    setRelease = JavaMethod("(Ljava/lang/Object;)V")
    compareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    compareAndExchange = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    compareAndExchangeAcquire = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    compareAndExchangeRelease = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    weakCompareAndSetPlain = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSetAcquire = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSetRelease = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    getAndSet = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    weakCompareAndSetVolatile = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    lazySet = JavaMethod("(Ljava/lang/Object;)V")
    getAndUpdate = JavaMethod("(Ljava/util/function/UnaryOperator;)Ljava/lang/Object;")
    updateAndGet = JavaMethod("(Ljava/util/function/UnaryOperator;)Ljava/lang/Object;")
    getAndAccumulate = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")
    accumulateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")
    getPlain = JavaMethod("()Ljava/lang/Object;")
    setPlain = JavaMethod("(Ljava/lang/Object;)V")