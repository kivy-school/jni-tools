from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RejectedExecutionHandler"]

class RejectedExecutionHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RejectedExecutionHandler"
    rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")