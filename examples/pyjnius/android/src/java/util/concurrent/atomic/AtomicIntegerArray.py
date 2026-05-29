from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicIntegerArray"]

class AtomicIntegerArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicIntegerArray"
    __javaconstructor__ = [("(I)V", False), ("([I)V", False)]
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    get = JavaMethod("(I)I")
    set = JavaMethod("(II)V")
    getOpaque = JavaMethod("(I)I")
    setOpaque = JavaMethod("(II)V")
    getAcquire = JavaMethod("(I)I")
    setRelease = JavaMethod("(II)V")
    compareAndSet = JavaMethod("(III)Z")
    compareAndExchange = JavaMethod("(III)I")
    compareAndExchangeAcquire = JavaMethod("(III)I")
    compareAndExchangeRelease = JavaMethod("(III)I")
    weakCompareAndSetPlain = JavaMethod("(III)Z")
    weakCompareAndSet = JavaMethod("(III)Z")
    weakCompareAndSetAcquire = JavaMethod("(III)Z")
    weakCompareAndSetRelease = JavaMethod("(III)Z")
    getAndSet = JavaMethod("(II)I")
    getAndAdd = JavaMethod("(II)I")
    incrementAndGet = JavaMethod("(I)I")
    weakCompareAndSetVolatile = JavaMethod("(III)Z")
    lazySet = JavaMethod("(II)V")
    getAndIncrement = JavaMethod("(I)I")
    getAndDecrement = JavaMethod("(I)I")
    decrementAndGet = JavaMethod("(I)I")
    addAndGet = JavaMethod("(II)I")
    getAndUpdate = JavaMethod("(ILjava/util/function/IntUnaryOperator;)I")
    updateAndGet = JavaMethod("(ILjava/util/function/IntUnaryOperator;)I")
    getAndAccumulate = JavaMethod("(IILjava/util/function/IntBinaryOperator;)I")
    accumulateAndGet = JavaMethod("(IILjava/util/function/IntBinaryOperator;)I")
    getPlain = JavaMethod("(I)I")
    setPlain = JavaMethod("(II)V")