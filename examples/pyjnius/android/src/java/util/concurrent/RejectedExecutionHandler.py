from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RejectedExecutionHandler"]

class RejectedExecutionHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RejectedExecutionHandler"
    rejectedExecution = JavaMethod("(Ljava/lang/Runnable;Ljava/util/concurrent/ThreadPoolExecutor;)V")