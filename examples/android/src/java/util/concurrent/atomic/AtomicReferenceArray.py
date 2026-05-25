from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicReferenceArray"]

class AtomicReferenceArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicReferenceArray"
    __javaconstructor__ = [("(I)V", False), ("([Ljava/lang/Object;)V", False)]
    length = JavaMethod("()I")
    get = JavaMethod("(I)Ljava/lang/Object;")
    set = JavaMethod("(ILjava/lang/Object;)V")
    lazySet = JavaMethod("(ILjava/lang/Object;)V")
    getAndSet = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    compareAndSet = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSet = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSetPlain = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Z")
    getAndUpdate = JavaMethod("(ILjava/util/function/UnaryOperator;)Ljava/lang/Object;")
    updateAndGet = JavaMethod("(ILjava/util/function/UnaryOperator;)Ljava/lang/Object;")
    getAndAccumulate = JavaMethod("(ILjava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")
    accumulateAndGet = JavaMethod("(ILjava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
    getPlain = JavaMethod("(I)Ljava/lang/Object;")
    setPlain = JavaMethod("(ILjava/lang/Object;)V")
    getOpaque = JavaMethod("(I)Ljava/lang/Object;")
    setOpaque = JavaMethod("(ILjava/lang/Object;)V")
    getAcquire = JavaMethod("(I)Ljava/lang/Object;")
    setRelease = JavaMethod("(ILjava/lang/Object;)V")
    compareAndExchange = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    compareAndExchangeAcquire = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    compareAndExchangeRelease = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    weakCompareAndSetVolatile = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSetAcquire = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSetRelease = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)Z")