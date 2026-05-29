from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Executor"]

class Executor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Executor"
    execute = JavaMethod("(Ljava/lang/Runnable;)V")