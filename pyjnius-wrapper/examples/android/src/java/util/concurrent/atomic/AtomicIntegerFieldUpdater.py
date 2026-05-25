from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicIntegerFieldUpdater"]

class AtomicIntegerFieldUpdater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicIntegerFieldUpdater"
    __javaconstructor__ = [("()V", False)]
    newUpdater = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Ljava/util/concurrent/atomic/AtomicIntegerFieldUpdater;")
    compareAndSet = JavaMethod("(Ljava/lang/Object;II)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;II)Z")
    set = JavaMethod("(Ljava/lang/Object;I)V")
    lazySet = JavaMethod("(Ljava/lang/Object;I)V")
    get = JavaMethod("(Ljava/lang/Object;)I")
    getAndSet = JavaMethod("(Ljava/lang/Object;I)I")
    getAndIncrement = JavaMethod("(Ljava/lang/Object;)I")
    getAndDecrement = JavaMethod("(Ljava/lang/Object;)I")
    getAndAdd = JavaMethod("(Ljava/lang/Object;I)I")
    incrementAndGet = JavaMethod("(Ljava/lang/Object;)I")
    decrementAndGet = JavaMethod("(Ljava/lang/Object;)I")
    addAndGet = JavaMethod("(Ljava/lang/Object;I)I")
    getAndUpdate = JavaMethod("(Ljava/lang/Object;Ljava/util/function/IntUnaryOperator;)I")
    updateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/util/function/IntUnaryOperator;)I")
    getAndAccumulate = JavaMethod("(Ljava/lang/Object;ILjava/util/function/IntBinaryOperator;)I")
    accumulateAndGet = JavaMethod("(Ljava/lang/Object;ILjava/util/function/IntBinaryOperator;)I")