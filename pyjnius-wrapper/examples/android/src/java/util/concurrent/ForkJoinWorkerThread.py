from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ForkJoinWorkerThread"]

class ForkJoinWorkerThread(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ForkJoinWorkerThread"
    __javaconstructor__ = [("(Ljava/util/concurrent/ForkJoinPool;)V", False)]
    getPool = JavaMethod("()Ljava/util/concurrent/ForkJoinPool;")
    getPoolIndex = JavaMethod("()I")
    onStart = JavaMethod("()V")
    onTermination = JavaMethod("(Ljava/lang/Throwable;)V")
    run = JavaMethod("()V")