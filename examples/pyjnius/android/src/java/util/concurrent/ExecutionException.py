from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecutionException"]

class ExecutionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ExecutionException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]