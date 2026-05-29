from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicLongFieldUpdater"]

class AtomicLongFieldUpdater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicLongFieldUpdater"
    newUpdater = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Ljava/util/concurrent/atomic/AtomicLongFieldUpdater;")
    get = JavaMethod("(Ljava/lang/Object;)J")
    set = JavaMethod("(Ljava/lang/Object;J)V")
    compareAndSet = JavaMethod("(Ljava/lang/Object;JJ)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;JJ)Z")
    getAndSet = JavaMethod("(Ljava/lang/Object;J)J")
    getAndAdd = JavaMethod("(Ljava/lang/Object;J)J")
    incrementAndGet = JavaMethod("(Ljava/lang/Object;)J")
    lazySet = JavaMethod("(Ljava/lang/Object;J)V")
    getAndIncrement = JavaMethod("(Ljava/lang/Object;)J")
    getAndDecrement = JavaMethod("(Ljava/lang/Object;)J")
    decrementAndGet = JavaMethod("(Ljava/lang/Object;)J")
    addAndGet = JavaMethod("(Ljava/lang/Object;J)J")
    getAndUpdate = JavaMethod("(Ljava/lang/Object;Ljava/util/function/LongUnaryOperator;)J")
    updateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/util/function/LongUnaryOperator;)J")
    getAndAccumulate = JavaMethod("(Ljava/lang/Object;JLjava/util/function/LongBinaryOperator;)J")
    accumulateAndGet = JavaMethod("(Ljava/lang/Object;JLjava/util/function/LongBinaryOperator;)J")