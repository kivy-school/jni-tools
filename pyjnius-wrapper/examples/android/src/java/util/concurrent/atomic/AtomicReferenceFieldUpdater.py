from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicReferenceFieldUpdater"]

class AtomicReferenceFieldUpdater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicReferenceFieldUpdater"
    __javaconstructor__ = [("()V", False)]
    newUpdater = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/Class;Ljava/lang/String;)Ljava/util/concurrent/atomic/AtomicReferenceFieldUpdater;")
    compareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z")
    set = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    lazySet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    getAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    getAndUpdate = JavaMethod("(Ljava/lang/Object;Ljava/util/function/UnaryOperator;)Ljava/lang/Object;")
    updateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/util/function/UnaryOperator;)Ljava/lang/Object;")
    getAndAccumulate = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")
    accumulateAndGet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BinaryOperator;)Ljava/lang/Object;")