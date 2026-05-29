from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicLongArray"]

class AtomicLongArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicLongArray"
    __javaconstructor__ = [("(I)V", False), ("([J)V", False)]
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    get = JavaMethod("(I)J")
    set = JavaMethod("(IJ)V")
    getOpaque = JavaMethod("(I)J")
    setOpaque = JavaMethod("(IJ)V")
    getAcquire = JavaMethod("(I)J")
    setRelease = JavaMethod("(IJ)V")
    compareAndSet = JavaMethod("(IJJ)Z")
    compareAndExchange = JavaMethod("(IJJ)J")
    compareAndExchangeAcquire = JavaMethod("(IJJ)J")
    compareAndExchangeRelease = JavaMethod("(IJJ)J")
    weakCompareAndSetPlain = JavaMethod("(IJJ)Z")
    weakCompareAndSet = JavaMethod("(IJJ)Z")
    weakCompareAndSetAcquire = JavaMethod("(IJJ)Z")
    weakCompareAndSetRelease = JavaMethod("(IJJ)Z")
    getAndSet = JavaMethod("(IJ)J")
    getAndAdd = JavaMethod("(IJ)J")
    incrementAndGet = JavaMethod("(I)J")
    weakCompareAndSetVolatile = JavaMethod("(IJJ)Z")
    lazySet = JavaMethod("(IJ)V")
    getAndIncrement = JavaMethod("(I)J")
    getAndDecrement = JavaMethod("(I)J")
    decrementAndGet = JavaMethod("(I)J")
    addAndGet = JavaMethod("(IJ)J")
    getAndUpdate = JavaMethod("(ILjava/util/function/LongUnaryOperator;)J")
    updateAndGet = JavaMethod("(ILjava/util/function/LongUnaryOperator;)J")
    getAndAccumulate = JavaMethod("(IJLjava/util/function/LongBinaryOperator;)J")
    accumulateAndGet = JavaMethod("(IJLjava/util/function/LongBinaryOperator;)J")
    getPlain = JavaMethod("(I)J")
    setPlain = JavaMethod("(IJ)V")