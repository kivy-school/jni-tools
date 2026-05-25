from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicLongFieldUpdater"]

class AtomicLongFieldUpdater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicLongFieldUpdater"
    __javaconstructor__ = [("()V", False)]
    newUpdater = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Ljava/util/concurrent/atomic/AtomicLongFieldUpdater;")
    compareAndSet = JavaMethod("(Ljava/lang/Object;JJ)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;JJ)Z")
    set = JavaMethod("(Ljava/lang/Object;J)V")
    lazySet = JavaMethod("(Ljava/lang/Object;J)V")
    get = JavaMethod("(Ljava/lang/Object;)J")
    getAndSet = JavaMethod("(Ljava/lang/Object;J)J")
    getAndIncrement = JavaMethod("(Ljava/lang/Object;)J")
    getAndDecrement = JavaMethod("(Ljava/lang/Object;)J")
    getAndAdd = JavaMethod("(Ljava/lang/Object;J)J")
    incrementAndGet = JavaMethod("(Ljava/lang/Object;)J")
    decrementAndGet = JavaMethod("(Ljava/lang/Object;)J")
    addAndGet = JavaMethod("(Ljava/lang/Object;J)J")
    getAndUpdate = JavaMethod("(Ljava/lang/Object;Ljava/util/function/LongUnaryOperator;)J")
    updateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/util/function/LongUnaryOperator;)J")
    getAndAccumulate = JavaMethod("(Ljava/lang/Object;JLjava/util/function/LongBinaryOperator;)J")
    accumulateAndGet = JavaMethod("(Ljava/lang/Object;JLjava/util/function/LongBinaryOperator;)J")