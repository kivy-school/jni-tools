from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicIntegerFieldUpdater"]

class AtomicIntegerFieldUpdater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicIntegerFieldUpdater"
    newUpdater = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Ljava/util/concurrent/atomic/AtomicIntegerFieldUpdater;")
    get = JavaMethod("(Ljava/lang/Object;)I")
    set = JavaMethod("(Ljava/lang/Object;I)V")
    compareAndSet = JavaMethod("(Ljava/lang/Object;II)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;II)Z")
    getAndSet = JavaMethod("(Ljava/lang/Object;I)I")
    getAndAdd = JavaMethod("(Ljava/lang/Object;I)I")
    incrementAndGet = JavaMethod("(Ljava/lang/Object;)I")
    lazySet = JavaMethod("(Ljava/lang/Object;I)V")
    getAndIncrement = JavaMethod("(Ljava/lang/Object;)I")
    getAndDecrement = JavaMethod("(Ljava/lang/Object;)I")
    decrementAndGet = JavaMethod("(Ljava/lang/Object;)I")
    addAndGet = JavaMethod("(Ljava/lang/Object;I)I")
    getAndUpdate = JavaMethod("(Ljava/lang/Object;Ljava/util/function/IntUnaryOperator;)I")
    updateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/util/function/IntUnaryOperator;)I")
    getAndAccumulate = JavaMethod("(Ljava/lang/Object;ILjava/util/function/IntBinaryOperator;)I")
    accumulateAndGet = JavaMethod("(Ljava/lang/Object;ILjava/util/function/IntBinaryOperator;)I")