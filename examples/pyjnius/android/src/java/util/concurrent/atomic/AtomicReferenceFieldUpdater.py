from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicReferenceFieldUpdater"]

class AtomicReferenceFieldUpdater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicReferenceFieldUpdater"
    newUpdater = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/Class;Ljava/lang/String;)Ljava/util/concurrent/atomic/AtomicReferenceFieldUpdater;")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    compareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z")
    getAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    lazySet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    getAndUpdate = JavaMethod("(Ljava/lang/Object;Ljava/util/function/UnaryOperator;)Ljava/lang/Object;")
    updateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/util/function/UnaryOperator;)Ljava/lang/Object;")
    getAndAccumulate = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")
    accumulateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")