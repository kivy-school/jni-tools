from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Executor"]

class Executor(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Executor"
    execute = JavaMethod("(Ljava/lang/Runnable;)V")