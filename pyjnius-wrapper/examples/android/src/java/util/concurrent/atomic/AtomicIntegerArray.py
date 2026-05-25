from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicIntegerArray"]

class AtomicIntegerArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicIntegerArray"
    __javaconstructor__ = [("(I)V", False), ("([I)V", False)]
    length = JavaMethod("()I")
    get = JavaMethod("(I)I")
    set = JavaMethod("(II)V")
    lazySet = JavaMethod("(II)V")
    getAndSet = JavaMethod("(II)I")
    compareAndSet = JavaMethod("(III)Z")
    weakCompareAndSet = JavaMethod("(III)Z")
    weakCompareAndSetPlain = JavaMethod("(III)Z")
    getAndIncrement = JavaMethod("(I)I")
    getAndDecrement = JavaMethod("(I)I")
    getAndAdd = JavaMethod("(II)I")
    incrementAndGet = JavaMethod("(I)I")
    decrementAndGet = JavaMethod("(I)I")
    addAndGet = JavaMethod("(II)I")
    getAndUpdate = JavaMethod("(ILjava/util/function/IntUnaryOperator;)I")
    updateAndGet = JavaMethod("(ILjava/util/function/IntUnaryOperator;)I")
    getAndAccumulate = JavaMethod("(IILjava/util/function/IntBinaryOperator;)I")
    accumulateAndGet = JavaMethod("(IILjava/util/function/IntBinaryOperator;)I")
    toString = JavaMethod("()Ljava/lang/String;")
    getPlain = JavaMethod("(I)I")
    setPlain = JavaMethod("(II)V")
    getOpaque = JavaMethod("(I)I")
    setOpaque = JavaMethod("(II)V")
    getAcquire = JavaMethod("(I)I")
    setRelease = JavaMethod("(II)V")
    compareAndExchange = JavaMethod("(III)I")
    compareAndExchangeAcquire = JavaMethod("(III)I")
    compareAndExchangeRelease = JavaMethod("(III)I")
    weakCompareAndSetVolatile = JavaMethod("(III)Z")
    weakCompareAndSetAcquire = JavaMethod("(III)Z")
    weakCompareAndSetRelease = JavaMethod("(III)Z")