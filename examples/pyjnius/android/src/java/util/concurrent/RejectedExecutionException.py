from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RejectedExecutionException"]

class RejectedExecutionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/RejectedExecutionException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]