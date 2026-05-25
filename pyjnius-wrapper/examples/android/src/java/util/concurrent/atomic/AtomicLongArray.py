from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicLongArray"]

class AtomicLongArray(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicLongArray"
    __javaconstructor__ = [("(I)V", False), ("([J)V", False)]
    length = JavaMethod("()I")
    get = JavaMethod("(I)J")
    set = JavaMethod("(IJ)V")
    lazySet = JavaMethod("(IJ)V")
    getAndSet = JavaMethod("(IJ)J")
    compareAndSet = JavaMethod("(IJJ)Z")
    weakCompareAndSet = JavaMethod("(IJJ)Z")
    weakCompareAndSetPlain = JavaMethod("(IJJ)Z")
    getAndIncrement = JavaMethod("(I)J")
    getAndDecrement = JavaMethod("(I)J")
    getAndAdd = JavaMethod("(IJ)J")
    incrementAndGet = JavaMethod("(I)J")
    decrementAndGet = JavaMethod("(I)J")
    addAndGet = JavaMethod("(IJ)J")
    getAndUpdate = JavaMethod("(ILjava/util/function/LongUnaryOperator;)J")
    updateAndGet = JavaMethod("(ILjava/util/function/LongUnaryOperator;)J")
    getAndAccumulate = JavaMethod("(IJLjava/util/function/LongBinaryOperator;)J")
    accumulateAndGet = JavaMethod("(IJLjava/util/function/LongBinaryOperator;)J")
    toString = JavaMethod("()Ljava/lang/String;")
    getPlain = JavaMethod("(I)J")
    setPlain = JavaMethod("(IJ)V")
    getOpaque = JavaMethod("(I)J")
    setOpaque = JavaMethod("(IJ)V")
    getAcquire = JavaMethod("(I)J")
    setRelease = JavaMethod("(IJ)V")
    compareAndExchange = JavaMethod("(IJJ)J")
    compareAndExchangeAcquire = JavaMethod("(IJJ)J")
    compareAndExchangeRelease = JavaMethod("(IJJ)J")
    weakCompareAndSetVolatile = JavaMethod("(IJJ)Z")
    weakCompareAndSetAcquire = JavaMethod("(IJJ)Z")
    weakCompareAndSetRelease = JavaMethod("(IJJ)Z")