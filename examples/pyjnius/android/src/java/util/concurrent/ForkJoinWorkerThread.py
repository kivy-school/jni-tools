from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ForkJoinWorkerThread"]

class ForkJoinWorkerThread(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ForkJoinWorkerThread"
    MIN_PRIORITY = JavaStaticField("I")
    NORM_PRIORITY = JavaStaticField("I")
    MAX_PRIORITY = JavaStaticField("I")
    run = JavaMethod("()V")
    getQueuedTaskCount = JavaMethod("()I")
    getPool = JavaMethod("()Ljava/util/concurrent/ForkJoinPool;")
    getPoolIndex = JavaMethod("()I")